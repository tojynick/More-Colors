from bpy.props import EnumProperty
from bpy.types import PropertyGroup


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
    
    gradient_range: EnumProperty(
        name = "Gradient Range Mode",
        description = "Determines where will be minimum and maximum positions of the gradient",
        items = [
            ("Per Object", "Range Per Object", "Only takes operated object's vertex positions into account. If several objects selected, each object will have its own range", "OBJECT_DATA", 1),
            ("Global", "Global Range", "Takes all selected object's vertex positions into account", "OUTLINER_COLLECTION", 2)
            ],
        default = "Global"
        )
    
    gradient_direction: EnumProperty(
        name = "Gradient Direction",
        description = "In what way the gradient will go",
        items = [
            ("X", "X Axis", ""),
            ("Inv_X", "-X Axis", ""),
            ("Y", "Y Axis", ""),
            ("Inv_Y", "-Y Axis", ""),
            ("Z", "Z Axis", ""),
            ("Inv_Z", "-Z Axis", "")
            ],
        default = "Z"
        )
