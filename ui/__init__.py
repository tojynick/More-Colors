import bpy

from .settings_panel import settings_panel, display_settings_panel, color_settings_panel
from .tools_panel import tools_panel, random_color_tool_panel, color_by_position_tool_panel
from . import about_panel

classes = (
    about_panel.MORECOLORS_PT_about_panel,
    settings_panel.MORECOLORS_PT_settings_panel,
    display_settings_panel.MORECOLORS_PT_display_settings_panel,
    tools_panel.MORECOLORS_PT_tools_panel,
    random_color_tool_panel.MORECOLORS_PT_random_color_tool_panel,
    color_settings_panel.MORECOLORS_PT_global_color_settings_panel,
    color_by_position_tool_panel.MORECOLORS_PT_random_color_tool_panel
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
