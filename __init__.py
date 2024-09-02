bl_info = {
    "name": "More Colors!",
    "author": "tojynick",
    "description": "A set of tools to make vertex painting easier.",
    "blender": (4, 0, 0),
    "version": (1, 0, 0),
    "location": "3D View > Sidebar > More Colors!",
    "tracker_url": "https://github.com/tojynick/More-Colors",
    "support": "COMMUNITY",
    "category": "Paint"
}

import bpy

from .operators import enable_object_mode, enable_vertex_paint, show_hide_vertex_colors, add_random_color

from .ui.settings_panel import settings_panel, display_settings_panel
from .ui.tools_panel import tools_panel, random_color_tool_panel

operator_classes = [
    enable_object_mode.MORECOLORS_OT_enable_object_mode,
    enable_vertex_paint.MORECOLORS_OT_enable_vertex_paint_mode,
    show_hide_vertex_colors.MORECOLORS_OT_show_vertex_colors,
    show_hide_vertex_colors.MORECOLORS_OT_hide_vertex_colors,
    add_random_color.MORECOLORS_OT_add_random_color
]

ui_classes = [
    settings_panel.MORECOLORS_PT_settings_panel,
    display_settings_panel.MORECOLORS_PT_display_settings_panel,
    tools_panel.MORECOLORS_PT_tools_panel,
    random_color_tool_panel.MORECOLORS_PT_random_color_tool_panel
]

property_group_classes = [
    add_random_color.RandomColorToolProperties
]

def register():
    for operator_class in operator_classes:
        bpy.utils.register_class(operator_class)

    for ui_class in ui_classes:
        bpy.utils.register_class(ui_class)

    for prop_group_class in property_group_classes:
        bpy.utils.register_class(prop_group_class)

    bpy.types.Scene.more_colors_random_color_tool = bpy.props.PointerProperty(type = add_random_color.RandomColorToolProperties)


def unregister():
    for operator_class in operator_classes:
        bpy.utils.unregister_class(operator_class)
    
    for ui_class in ui_classes:
        bpy.utils.unregister_class(ui_class)

    for prop_group_class in property_group_classes:
        bpy.utils.unregister_class(prop_group_class)

    del bpy.types.Scene.more_colors_random_color_tool