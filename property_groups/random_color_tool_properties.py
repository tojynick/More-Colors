from bpy.props import EnumProperty
from bpy.types import PropertyGroup


class RandomColorToolProperties(PropertyGroup):
    element_type: EnumProperty(
        name = "Element",
        description = "Elements to generate colors on",
        items = [
            ("Point", "Per Point", "Points are shared across faces"),
            ("Vertex", "Per Vertex", "Vertices are unique per face"),
            ("Face", "Per Face", "")
            ]
        )
    