
import bpy

from . import enable_object_mode, enable_vertex_paint, reset_vertex_colors, show_hide_vertex_colors, add_random_color, open_documentation, add_color_by_position

classes = (
    enable_object_mode.MORECOLORS_OT_enable_object_mode,
    enable_vertex_paint.MORECOLORS_OT_enable_vertex_paint_mode,
    show_hide_vertex_colors.MORECOLORS_OT_show_vertex_colors,
    show_hide_vertex_colors.MORECOLORS_OT_hide_vertex_colors,
    add_random_color.MORECOLORS_OT_add_random_color,
    open_documentation.MORECOLORS_OT_open_documentation,
    reset_vertex_colors.MORECOLORS_OT_reset_color,
    add_color_by_position.MORECOLORS_OT_add_color_by_position
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
