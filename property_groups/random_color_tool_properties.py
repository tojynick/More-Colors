from bpy.props import EnumProperty
from bpy.types import PropertyGroup

class RandomColorToolProperties(PropertyGroup):
    element_type: EnumProperty(
        name = "Element",
        description = "Elements to generate colors on",
        items = [
            ("Point", "Per Point", "Points are shared across faces", "DECORATE", 1),
            ("Vertex", "Per Vertex", "Vertices are unique per face", "VERTEXSEL", 2),
            ("Face", "Per Face", "Faces are well... faces", "SNAP_FACE", 3)
            ]
        )
    
    color_mode: EnumProperty(
        name = "Random Color Mode",
        description = "Color generation method",
        items = [
            ("RGBA", "RGB", "Randomizes color by RGBA values."),
            ("Hue", "Hue", "Randomizes color only by hue. Saturation and alpha will be 1, lightness will be 0.5")
            ]
        )
    