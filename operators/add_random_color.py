from ..utilities.get_random_color import get_random_color
from .base_operator import BaseOperator
import bpy
from bpy.types import PropertyGroup


class RandomColorToolProperties(PropertyGroup):
    element_type: bpy.props.EnumProperty(
        name = "Element",
        description = "Elements to generate colors on",
        items = [
            ("Point", "Per Point", "Points are shared across faces"),
            ("Vertex", "Per Vertex", "Vertices are unique per face"),
            ("Face", "Per Face", "")
            ]
        )
    

def add_random_color_per_point(mesh, vertex_colors):
    point_colors = {}

    for vertex in mesh.vertices:
        point_colors[vertex.index] = get_random_color()
    
    for face in mesh.polygons:
        for loop_index in face.loop_indices:
            vertex_index = mesh.loops[loop_index].vertex_index
            vertex_colors.data[loop_index].color = point_colors[vertex_index]


def add_random_color_per_vertex(mesh, vertex_colors):
    for face in mesh.polygons:
        for loop_index in face.loop_indices:
            vertex_colors.data[loop_index].color = get_random_color()


def add_random_color_per_face(mesh, vertex_colors):
    for face in mesh.polygons:
        random_color = get_random_color()

        for loop_index in face.loop_indices:
            vertex_colors.data[loop_index].color = random_color


class MORECOLORS_OT_add_random_color(BaseOperator):
    """Adds a random vertex color for each vertex to the selected mesh"""
    bl_label = "Add Random Color"
    bl_idname = "morecolors.add_random_color"

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "elements_enum")

    @classmethod
    def poll(cls, context):
        return len(context.selected_objects) > 0 and bpy.context.object.mode == "OBJECT"    

    def execute(self, context):
        scene = context.scene
        tool = scene.more_colors_random_color_tool

        if len(context.selected_objects) == 0:
            self.report({"ERROR"}, "No objects selected!")
            return {"CANCELLED"}
        
        for obj in context.selected_objects:
            if obj.type != "MESH":
                continue
            
            mesh = obj.data
            
            if not mesh.vertex_colors:
                vertex_colors = mesh.vertex_colors.new(name = "Attribute")
            else:
                vertex_colors = mesh.vertex_colors.active

            match tool.element_type:
                case "Point":
                    add_random_color_per_point(mesh, vertex_colors)
                case "Vertex":
                    add_random_color_per_vertex(mesh, vertex_colors)
                case "Face":
                    add_random_color_per_face(mesh, vertex_colors)
            
            self.report({"INFO"}, "Random vertex color applied!")

        return {"FINISHED"}