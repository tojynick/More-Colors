from bpy.props import StringProperty
from bpy.types import PropertyGroup

class ShowHideVertexColorsProperties(PropertyGroup):
    previous_shading_type: StringProperty(name = "Previous Shading Type", default = "SOLID")
    previous_color_type: StringProperty(name = "Previous Color Type", default = "OBJECT")
    previous_light_type: StringProperty(name = "Previous Light Type", default = "STUDIO")