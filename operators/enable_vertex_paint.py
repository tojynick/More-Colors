import bpy
from .base_operator import BaseOperator

class MORECOLORS_OT_enable_vertex_paint_mode(BaseOperator):
    bl_label = "Switch To Vertex Paint Mode"
    bl_idname = "morecolors.enable_vertex_paint_mode"

    def execute(self, context):
        context.space_data.shading.type = "SOLID"
        bpy.ops.object.mode_set(mode = "VERTEX_PAINT")

        return {"FINISHED"}
