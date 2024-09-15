from .base_operators import BaseColorOperator
from ..utilities.color_utilities import get_masked_color
import bmesh

class MORECOLORS_OT_add_color_by_position(BaseColorOperator):
    """Adds a color based on vertex position for each selected mesh object"""
    
    bl_label = "Add Color By Position"
    bl_idname = "morecolors.add_color_by_position"
    
    def execute(self, context):
        if not context.selected_objects:
            self.report({"ERROR"}, "No objects selected!")
            return {"CANCELLED"}
        
        scene = context.scene
        global_color_settings = scene.more_colors_global_color_settings
        color_by_position_tool = scene.more_colors_color_by_position_tool

        gradient_direction = color_by_position_tool.gradient_direction
        axis_index = {"X": 0, "Y": 1, "Z": 2}[gradient_direction[-1]]

        # Reverse direction names always have more than one letter in the name
        reverse_gradient = len(gradient_direction) > 1  

        for obj in context.selected_objects:
            if obj.type != "MESH":
                continue
            
            mesh = obj.data
            if not mesh.vertex_colors:
                mesh.vertex_colors.new(name = "Attribute")

            bm = bmesh.new()
            bm.from_mesh(mesh)
            color_layer = bm.loops.layers.color.active

            vertex_positions = [obj.matrix_world @ v.co if color_by_position_tool.space_type == "World" else v.co for v in bm.verts]

            # Calculate min and max based on the axis
            positions_along_axis = [pos[axis_index] for pos in vertex_positions]
            min_pos = min(positions_along_axis)
            max_pos = max(positions_along_axis)

            # Avoid cases, where max and min pos are the same
            range = max(max_pos - min_pos, 1)  

            for face in bm.faces:
                for loop in face.loops:
                    vert_index = loop.vert.index
                    pos_value = vertex_positions[vert_index][axis_index]

                    gradient_value = (pos_value - min_pos) / range
                    
                    if reverse_gradient:
                        gradient_value = 1 - gradient_value

                    color = (gradient_value, gradient_value, gradient_value, 1)
                    loop[color_layer] = get_masked_color(loop[color_layer], color, global_color_settings.get_mask())

            bm.to_mesh(mesh)
            bm.free()
            obj.data.update()

        self.report({"INFO"}, "Vertex colors assigned successfully!")
        return {"FINISHED"}
