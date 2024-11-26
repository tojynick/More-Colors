from bpy.types import PropertyGroup

from bpy.props import EnumProperty
from bpy.props import StringProperty


class ColorByPositionToolProperties(PropertyGroup):
    space_type: EnumProperty(
        name = "Space",
        description = "In what space color will be generated",
        items = [
            ("Local", "Local Space", "", "ORIENTATION_LOCAL", 1),
            ("World", "World Space", "", "WORLD", 2)
            ],
        default = "World"
        )
    
    gradient_direction: EnumProperty(
        name = "Gradient Direction",
        description = "In what way the gradient will go",
        items = [
            ("X", "X Axis", ""),
            ("-X", "-X Axis", ""),
            ("Y", "Y Axis", ""),
            ("-Y", "-Y Axis", ""),
            ("Z", "Z Axis", ""),
            ("-Z", "-Z Axis", "")
            ],
        default = "Z"
        )
    
    color_ramp_material_name: StringProperty(name = "Color Ramp Material Name", default = "MORECOLORS_ColorByPositionRamp")
