from ..utilities.color_utilities import get_masked_color, get_random_color
from .base_operators import BaseColorOperator
import bpy


class MORECOLORS_OT_add_random_color(BaseColorOperator):
    """Adds a random vertex color for each vertex to the selected mesh"""
    bl_label = "Add Random Color"
    bl_idname = "morecolors.add_random_color"

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "elements_enum")

    @classmethod
    def poll(cls, context):
        return len(context.selected_objects) > 0 and bpy.context.object.mode == "OBJECT"


    def add_random_color_per_face(self, mesh, vertex_colors, global_color_settings, random_color_tool):
        for face in mesh.polygons:
            random_color = get_random_color(random_color_tool.color_mode)

            for loop_index in face.loop_indices:
                vertex_colors.data[loop_index].color = get_masked_color(vertex_colors.data[loop_index].color, random_color, global_color_settings.get_mask())

    
    def add_random_color_per_point(self, mesh, vertex_colors, global_color_settings, random_color_tool):
        point_colors = {}

        for vertex in mesh.vertices:
            point_colors[vertex.index] = get_random_color(random_color_tool.color_mode)
        
        for face in mesh.polygons:
            for loop_index in face.loop_indices:
                vertex_index = mesh.loops[loop_index].vertex_index
                vertex_colors.data[loop_index].color = get_masked_color(vertex_colors.data[loop_index].color, point_colors[vertex_index], global_color_settings.get_mask())
    

    def add_random_color_per_vertex(self, mesh, vertex_colors, global_color_settings, random_color_tool):
        for face in mesh.polygons:
            for loop_index in face.loop_indices:
                vertex_colors.data[loop_index].color = get_masked_color(vertex_colors.data[loop_index].color, get_random_color(random_color_tool.color_mode), global_color_settings.get_mask())


    def execute(self, context):
        scene = context.scene
        random_color_tool = scene.more_colors_random_color_tool
        global_color_settings = scene.more_colors_gloabal_color_settings

        if len(context.selected_objects) == 0:
            self.report({"ERROR"}, "No objects selected!")
            return {"CANCELLED"}
        
        for obj in context.selected_objects:
            if obj.type != "MESH":
                continue
            
            mesh = obj.data
            
            if not mesh.vertex_colors:
                vertex_colors = mesh.vertex_colors.new(name = "Attribute")
            else:
                vertex_colors = mesh.vertex_colors.active

            match random_color_tool.element_type:
                case "Point":
                    self.add_random_color_per_point(mesh, vertex_colors, global_color_settings, random_color_tool)
                case "Vertex":
                    self.add_random_color_per_vertex(mesh, vertex_colors, global_color_settings, random_color_tool)
                case "Face":
                    self.add_random_color_per_face(mesh, vertex_colors, global_color_settings, random_color_tool)
            
            self.report({"INFO"}, "Random vertex color applied!")

        return {"FINISHED"}
