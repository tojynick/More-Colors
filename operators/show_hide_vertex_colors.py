from .base_operator import BaseOperator

class MORECOLORS_OT_show_vertex_colors(BaseOperator):
    bl_label = "Show Vertex Colors"
    bl_idname = "morecolors.show_vertex_colors"

    def execute(self, context):
        context.space_data.shading.type = "SOLID"
        context.space_data.shading.color_type = "VERTEX"
        context.space_data.shading.light = "FLAT"

        return {"FINISHED"}


class MORECOLORS_OT_hide_vertex_colors(BaseOperator):
    bl_label = "Hide Vertex Colors"
    bl_idname = "morecolors.hide_vertex_colors"

    def execute(self, context):
        context.space_data.shading.type = "SOLID"
        context.space_data.shading.color_type = "OBJECT"
        context.space_data.shading.light = "STUDIO"

        return {"FINISHED"}
