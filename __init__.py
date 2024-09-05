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

from .utilities.icon_loader import IconsLoader

from .operators import enable_object_mode, enable_vertex_paint, reset_vertex_colors, show_hide_vertex_colors, add_random_color, open_documentation, add_color_by_position
from .property_groups import random_color_tool_properties, global_color_settings_properties, color_by_position_tool_properties

from .ui.settings_panel import settings_panel, display_settings_panel, color_settings_panel
from .ui.tools_panel import tools_panel, random_color_tool_panel, color_by_position_tool_panel
from .ui import about_panel


operator_classes = [
    enable_object_mode.MORECOLORS_OT_enable_object_mode,
    enable_vertex_paint.MORECOLORS_OT_enable_vertex_paint_mode,
    show_hide_vertex_colors.MORECOLORS_OT_show_vertex_colors,
    show_hide_vertex_colors.MORECOLORS_OT_hide_vertex_colors,
    add_random_color.MORECOLORS_OT_add_random_color,
    open_documentation.MORECOLORS_OT_open_documentation,
    reset_vertex_colors.MORECOLORS_OT_reset_color,
    add_color_by_position.MORECOLORS_OT_add_color_by_position
]

ui_classes = [
    about_panel.MORECOLORS_PT_about_panel,
    settings_panel.MORECOLORS_PT_settings_panel,
    display_settings_panel.MORECOLORS_PT_display_settings_panel,
    tools_panel.MORECOLORS_PT_tools_panel,
    random_color_tool_panel.MORECOLORS_PT_random_color_tool_panel,
    color_settings_panel.MORECOLORS_PT_global_color_settings_panel,
    color_by_position_tool_panel.MORECOLORS_PT_random_color_tool_panel
]

property_group_classes = [
    random_color_tool_properties.RandomColorToolProperties,
    global_color_settings_properties.GlobalColorSettingsProperties,
    color_by_position_tool_properties.ColorByPositionToolProperties
]


def register():
    # Register classes
    for operator_class in operator_classes:
        bpy.utils.register_class(operator_class)

    for ui_class in ui_classes:
        bpy.utils.register_class(ui_class)

    for prop_group_class in property_group_classes:
        bpy.utils.register_class(prop_group_class)

    bpy.types.Scene.more_colors_random_color_tool = bpy.props.PointerProperty(type = random_color_tool_properties.RandomColorToolProperties)
    bpy.types.Scene.more_colors_global_color_settings = bpy.props.PointerProperty(type = global_color_settings_properties.GlobalColorSettingsProperties)
    bpy.types.Scene.more_colors_color_by_position_tool = bpy.props.PointerProperty(type = color_by_position_tool_properties.ColorByPositionToolProperties)

    # Register icons    
    bpy.types.Scene.preview_collection = bpy.utils.previews.new()
    IconsLoader.register_custom_icons()


def unregister():
    # Unregister classes
    for operator_class in operator_classes:
        bpy.utils.unregister_class(operator_class)
    
    for ui_class in ui_classes:
        bpy.utils.unregister_class(ui_class)

    for prop_group_class in property_group_classes:
        bpy.utils.unregister_class(prop_group_class)

    del bpy.types.Scene.more_colors_random_color_tool
    del bpy.types.Scene.more_colors_global_color_settings
    del bpy.types.Scene.more_colors_color_by_position_tool

    # Unrefister icons
    bpy.utils.previews.remove(bpy.types.Scene.preview_collection)
    del bpy.types.Scene.preview_collection
