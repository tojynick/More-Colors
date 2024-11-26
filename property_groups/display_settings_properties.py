import bpy
from bpy.props import StringProperty
from bpy.props import EnumProperty
from bpy.types import PropertyGroup


def on_settings_update(self, context):
    bpy.ops.morecolors.display_vertex_colors()
    

class DisplaySettingsProperties(PropertyGroup):
    previous_shading_type: StringProperty(name = "Previous Shading Type", default = "SOLID")
    previous_color_type: StringProperty(name = "Previous Color Type", default = "OBJECT")
    previous_light_type: StringProperty(name = "Previous Light Type", default = "STUDIO")

    display_mode: EnumProperty(
        name = "Vertex Colors Display Mode",
        description = "Determines how vertex colors will be presented",
        items = [
            ("Off", "Off", "Do not show vertex color."),
            ("RGB", "RGB", "Show only RGB components of vertex colors."),
            ("Alpha", "Alpha", "Show only alpha component of vertex colors.")
            ],
        default = "Off",
        update = on_settings_update
        )
    
