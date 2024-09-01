import bpy
from . import utils
from bpy.types import Operator

class MORECOLORS_OT_add_random_color(Operator):
    """Adds a random vertex color for each vertex to the selected mesh"""
    bl_label = "Add Random Color"
    bl_idname = "morecolors.add_random_color"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        obj = context.active_object
        
        if obj is None or obj.type != "MESH":
            self.report({"WARNING"}, "No mesh object selected!")
            return {"CANCELLED"}
        
        mesh = obj.data
        # Check if object has colors, if not, add a layer
        if not mesh.vertex_colors:
            vertex_colors = mesh.vertex_colors.new(name = "Attribute")
        # Otherwise use existing one
        else:
            vertex_colors = mesh.vertex_colors.active

        color_data = [0.0] * (len(vertex_colors.data) * 4)
        
        for face in mesh.polygons:

            random_color = utils.get_random_color()

            for loop_index in face.loop_indices:
                vertex_colors.data[loop_index].color = random_color
        
        self.report({"INFO"}, "Random vertex color applied!")
        return {"FINISHED"}