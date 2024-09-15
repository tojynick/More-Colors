from bpy.props import FloatVectorProperty
from bpy.types import PropertyGroup

class SimpleFillToolProperties(PropertyGroup):

    selected_color: FloatVectorProperty(
        name = "Color",
        description = "Choose a color",
        subtype = "COLOR",
        default = (1, 1, 1, 1),
        min = 0, 
        max = 1,
        size = 4
    )

    preset_color_1: FloatVectorProperty(
        name = "Preset Color 1",
        description = "Choose a color",
        subtype = "COLOR",
        default = (1, 0, 0.03, 1),
        min = 0, 
        max = 1,
        size = 4
    )

    preset_color_2: FloatVectorProperty(
        name = "Preset Color 2",
        description = "Choose a color",
        subtype = "COLOR",
        default = (1, 0.730, 0, 1),
        min = 0, 
        max = 1,
        size = 4
    )

    preset_color_3: FloatVectorProperty(
            name = "Preset Color 3",
            description = "Choose a color",
            subtype = "COLOR",
            default = (0.483, 0.788, 0, 1),
            min = 0, 
            max = 1,
            size = 4
        )

    preset_color_4: FloatVectorProperty(
            name = "Preset Color 4",
            description = "Choose a color",
            subtype = "COLOR",
            default = (0, 0.475, 0.768, 1),
            min = 0, 
            max = 1,
            size = 4
        )
