from ..utilities.color_utilities import get_masked_color, get_random_color
from .base_operators import BaseColorOperator
import bpy
import bmesh

class MORECOLORS_OT_add_random_color(BaseColorOperator):
    """Adds a random color per chosen element (point, vertex, face) for each selected mesh object"""

    bl_label = "Add Random Color"
    bl_idname = "morecolors.add_random_color"

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "elements_enum")


    @classmethod
    def poll(cls, context):
        return len(context.selected_objects) > 0 and bpy.context.object.mode == "OBJECT"


    def add_random_color_per_face(self, bm, color_layer, global_color_settings, random_color_tool):
        for face in bm.faces:
            random_color = get_random_color(random_color_tool.color_mode)

            for loop in face.loops:
                loop[color_layer] = get_masked_color(loop[color_layer], random_color, global_color_settings.get_mask())

    
    def add_random_color_per_point(self, bm, color_layer, global_color_settings, random_color_tool):
        point_colors = {}

        for vertex in bm.verts:
            point_colors[vertex.index] = get_random_color(random_color_tool.color_mode)
        
        for face in bm.faces:
            for loop in face.loops:
                loop[color_layer] = get_masked_color(loop[color_layer], point_colors[loop.vert.index], global_color_settings.get_mask())
    

    def add_random_color_per_vertex(self, bm, color_layer, global_color_settings, random_color_tool):
        for face in bm.faces:
            for loop in face.loops:
                random_color = get_random_color(random_color_tool.color_mode)
                loop[color_layer] = get_masked_color(loop[color_layer], random_color, global_color_settings.get_mask())
    
    
    def add_random_color_per_island(self, bm, color_layer, global_color_settings, random_color_tool):
        island_faces = []
        visited_faces = set()

        def get_connected_faces(face):
            """Recursively collects all faces connected to the given face"""

            stack = [face]
            connected_faces = set()

            while stack:
                current_face = stack.pop()

                if current_face in visited_faces:
                    continue

                visited_faces.add(current_face)
                connected_faces.add(current_face)

                # Add neighboring faces (sharing edges)
                for edge in current_face.edges:
                    for linked_face in edge.link_faces:
                        if linked_face not in visited_faces:
                            stack.append(linked_face)

            return connected_faces

        # Find linked face islands
        for face in bm.faces:
            if face not in visited_faces:
                connected_faces = get_connected_faces(face)
                island_faces.append(connected_faces)

        # Assign random color to each island
        for component in island_faces:
            random_color = get_random_color(random_color_tool.color_mode)

            for face in component:
                for loop in face.loops:
                    loop[color_layer] = get_masked_color(loop[color_layer], random_color, global_color_settings.get_mask())


    def execute(self, context):
        scene = context.scene
        random_color_tool = scene.more_colors_random_color_tool
        global_color_settings = scene.more_colors_global_color_settings

        if len(context.selected_objects) == 0:
            self.report({"ERROR"}, "No objects selected!")
            return {"CANCELLED"}
        
        for obj in context.selected_objects:
            if obj.type != "MESH":
                continue
            
            mesh = obj.data
            
            if not mesh.vertex_colors:
                mesh.vertex_colors.new(name = "Attribute")

            bm = bmesh.new()
            bm.from_mesh(mesh)
            
            color_layer = bm.loops.layers.color.active

            match random_color_tool.element_type:
                case "Point":
                    self.add_random_color_per_point(bm, color_layer, global_color_settings, random_color_tool)
                case "Vertex":
                    self.add_random_color_per_vertex(bm, color_layer, global_color_settings, random_color_tool)
                case "Face":
                    self.add_random_color_per_face(bm, color_layer, global_color_settings, random_color_tool)
                case "Island":
                    self.add_random_color_per_island(bm, color_layer, global_color_settings, random_color_tool)

            bm.to_mesh(mesh)
            bm.free()

            obj.data.update()
            
            self.report({"INFO"}, "Random vertex color applied!")

        return {"FINISHED"}
