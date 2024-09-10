import bpy

from . import random_color_tool_properties, global_color_settings_properties, color_by_position_tool_properties

classes = (
    random_color_tool_properties.RandomColorToolProperties,
    global_color_settings_properties.GlobalColorSettingsProperties,
    color_by_position_tool_properties.ColorByPositionToolProperties
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    
    bpy.types.Scene.more_colors_random_color_tool = bpy.props.PointerProperty(type = random_color_tool_properties.RandomColorToolProperties)
    bpy.types.Scene.more_colors_global_color_settings = bpy.props.PointerProperty(type = global_color_settings_properties.GlobalColorSettingsProperties)
    bpy.types.Scene.more_colors_color_by_position_tool = bpy.props.PointerProperty(type = color_by_position_tool_properties.ColorByPositionToolProperties)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

    del bpy.types.Scene.more_colors_random_color_tool
    del bpy.types.Scene.more_colors_global_color_settings
    del bpy.types.Scene.more_colors_color_by_position_tool
