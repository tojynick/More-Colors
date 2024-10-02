from .base_operators import BaseOperator

class MORECOLORS_OT_show_vertex_colors(BaseOperator):
    """Enables vertex colors preview in the 3d viewport"""

    bl_label = "Show Vertex Colors"
    bl_idname = "morecolors.show_vertex_colors"

    def execute(self, context):
        settings = context.scene.more_colors_show_hide_color_settings

        settings.previous_shading_type = context.space_data.shading.type
        settings.previous_color_type = context.space_data.shading.color_type
        settings.previous_light_type =  context.space_data.shading.light

        context.space_data.shading.type = "SOLID"
        context.space_data.shading.color_type = "VERTEX"
        context.space_data.shading.light = "FLAT"

        return {"FINISHED"}


class MORECOLORS_OT_hide_vertex_colors(BaseOperator):
    bl_label = "Hide Vertex Colors"
    bl_idname = "morecolors.hide_vertex_colors"

    def execute(self, context):
        settings = context.scene.more_colors_show_hide_color_settings

        context.space_data.shading.type = settings.previous_shading_type
        context.space_data.shading.color_type = settings.previous_color_type
        context.space_data.shading.light =  settings.previous_light_type

        return {"FINISHED"}
