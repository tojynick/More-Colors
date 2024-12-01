from ..utilities.color_utilities import get_masked_color, get_random_color, get_active_color_attribute
from .base_operators import BaseColorOperator

class MORECOLORS_OT_add_random_color(BaseColorOperator):
    """Adds a random color per chosen element (point, vertex, face) for each selected mesh object"""

    bl_label = "Add Random Color"
    bl_idname = "morecolors.add_random_color"


    @classmethod
    def poll(cls, context):

        if len(context.selected_objects) == 0:
            return False
        
        if context.object.mode != "OBJECT":
            return False

        for obj in context.selected_objects:
            if obj.type != "MESH":
                return False
            
        return True

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "elements_enum")
        

    def add_random_color_per_face(self, obj, color_attribute, global_color_settings, random_color_tool):
        for poly in obj.data.polygons:
            random_color = get_random_color(random_color_tool.color_mode)

            for loop_index in poly.loop_indices:
                data = color_attribute.data[loop_index]              
                data.color_srgb = get_masked_color(data.color_srgb, random_color, global_color_settings.get_mask())

    
    def add_random_color_per_point(self, obj, color_attribute, global_color_settings, random_color_tool):
        for vert in obj.data.vertices:
            random_color = get_random_color(random_color_tool.color_mode)

            for poly in obj.data.polygons:
                for loop_index in poly.loop_indices:

                    # Check if the loop belongs to the selected vertex
                    loop_vert_index = obj.data.loops[loop_index].vertex_index
                    if loop_vert_index == vert.index:  
                        data = color_attribute.data[loop_index]
                        data.color_srgb = get_masked_color(data.color_srgb, random_color, global_color_settings.get_mask())
    

    def add_random_color_per_vertex(self, color_attribute, global_color_settings, random_color_tool):
        random_color = get_random_color(random_color_tool.color_mode)

        for data in color_attribute.data:
            random_color = get_random_color(random_color_tool.color_mode)
            data.color_srgb = get_masked_color(data.color_srgb, random_color, global_color_settings.get_mask())


    def add_random_color_per_island(self, obj, color_attribute, global_color_settings, random_color_tool):

        def get_connected_faces(face_index, visited_faces, adjacency_list):
            connected_faces = {face_index}
            faces_to_check = [face_index]
            
            while faces_to_check:
                current_face = faces_to_check.pop()
                for neighbor in adjacency_list[current_face]:
                    if neighbor not in visited_faces:
                        visited_faces.add(neighbor)
                        connected_faces.add(neighbor)
                        faces_to_check.append(neighbor)
                        
            return connected_faces

        adjacency_list = {i: [] for i in range(len(obj.data.polygons))}
        for edge in obj.data.edges:
            edge_faces = []
            for polygon_index, polygon in enumerate(obj.data.polygons):
                if all(vertex in polygon.vertices for vertex in edge.vertices):
                    edge_faces.append(polygon_index)
            for i in range(len(edge_faces)):
                for j in range(i + 1, len(edge_faces)):
                    adjacency_list[edge_faces[i]].append(edge_faces[j])
                    adjacency_list[edge_faces[j]].append(edge_faces[i])

        visited_faces = set()
        for face_index in range(len(obj.data.polygons)):
            if face_index not in visited_faces:
                connected_faces = get_connected_faces(face_index, visited_faces, adjacency_list)
                random_color = get_random_color(random_color_tool.color_mode)
                
                for connected_face_index in connected_faces:
                    poly = obj.data.polygons[connected_face_index]
                    for loop_index in poly.loop_indices:
                        data = color_attribute.data[loop_index]
                        data.color_srgb = get_masked_color(data.color_srgb, random_color, global_color_settings.get_mask())


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
            
            color_attribute = get_active_color_attribute(obj)

            match color_attribute.domain:

                # On point domain color is stored for each point, not for each vertex, 
                # therefore we're don't need to check for selected random_color_tool.element_type
                case "POINT":
                    for p in obj.data.vertices:
                        data = color_attribute.data[p.index]
                        random_color = get_random_color(random_color_tool.color_mode)
                        data.color_srgb = get_masked_color(data.color_srgb, random_color, global_color_settings.get_mask())
                
                case "CORNER":
                    match random_color_tool.element_type:
                        case "Point":
                            self.add_random_color_per_point(obj, color_attribute, global_color_settings, random_color_tool)
                        case "Vertex":
                            self.add_random_color_per_vertex(color_attribute, global_color_settings, random_color_tool)
                        case "Face":
                            self.add_random_color_per_face(obj, color_attribute, global_color_settings, random_color_tool)
                        case "Island":
                            self.add_random_color_per_island(obj, color_attribute, global_color_settings, random_color_tool)

            obj.data.update()
            
            self.report({"INFO"}, "Random vertex color applied!")

        return {"FINISHED"}
