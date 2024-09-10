from .base_operators import BaseColorOperator
from ..utilities.color_utilities import get_masked_color
import bpy
import bmesh

class MORECOLORS_OT_add_color_by_position(BaseColorOperator):

    bl_label = "Add Color By Position"
    bl_idname = "morecolors.add_color_by_position"
    
    def execute(self, context):
        if len(context.selected_objects) == 0:
            self.report({"ERROR"}, "No objects selected!")
            return {"CANCELLED"}
        
        scene = context.scene
        global_color_settings = scene.more_colors_global_color_settings
        color_by_position_tool = scene.more_colors_color_by_position_tool

        
        for obj in context.selected_objects:
            if obj.type != "MESH":
                continue
            
            mesh = obj.data

            if not mesh.vertex_colors:
                mesh.vertex_colors.new(name = "Attribute")

            bm = bmesh.new()
            bm.from_mesh(mesh)

            color_layer = bm.loops.layers.color.active

            match color_by_position_tool.space_type:
                case "Local":
                    vertex_positions = [v.co for v in bm.verts]
                case "World":
                     # Convert local vertex positions to world positions using object's transform
                    vertex_positions = [obj.matrix_world @ v.co for v in bm.verts]

            if color_by_position_tool.gradient_direction == "X" or color_by_position_tool.gradient_direction == "-X":
                min_pos = min(v.x for v in vertex_positions)
                max_pos = max(v.x for v in vertex_positions)
            elif color_by_position_tool.gradient_direction == "Y" or color_by_position_tool.gradient_direction == "-Y":
                min_pos = min(v.y for v in vertex_positions)
                max_pos = max(v.y for v in vertex_positions)
            elif color_by_position_tool.gradient_direction == "Z" or color_by_position_tool.gradient_direction == "-Z":
                min_pos = min(v.z for v in vertex_positions)
                max_pos = max(v.z for v in vertex_positions)

            if max_pos == min_pos:
                range = 1
            else:
                range = max_pos - min_pos

            for face in bm.faces:
                for loop in face.loops:
                    vert_index = loop.vert.index

                    if color_by_position_tool.gradient_direction == "X" or color_by_position_tool.gradient_direction == "-X":
                        pos = vertex_positions[vert_index].x
                    elif color_by_position_tool.gradient_direction == "Y" or color_by_position_tool.gradient_direction == "-Y":
                        pos = vertex_positions[vert_index].y
                    elif color_by_position_tool.gradient_direction == "Z" or color_by_position_tool.gradient_direction == "-Z":
                        pos = vertex_positions[vert_index].z

                    gradient_value = (pos - min_pos) / range

                    # Positive directions always have 1 letter (X, Y, Z)
                    if len(color_by_position_tool.gradient_direction) > 1:
                        gradient_value = 1 - gradient_value

                    color = (gradient_value, gradient_value, gradient_value, 1)
                    loop[color_layer] = get_masked_color((0,0,0,0), color, global_color_settings.get_mask())
            

            bm.to_mesh(mesh)
            bm.free()
            
            obj.data.update()
            
            self.report({"INFO"}, "Vertex colors assigned successfully")

        return {"FINISHED"}
