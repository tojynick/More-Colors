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
        
        for obj in context.selected_objects:
            if obj.type != "MESH":
                continue
            
            mesh = obj.data
            
            if not mesh.vertex_colors:
                mesh.vertex_colors.new(name = "Attribute")


            bm = bmesh.new()
            bm.from_mesh(mesh)

            color_layer = bm.loops.layers.color.active

            # Convert local vertex positions to world positions using object's transform
            world_verts = [obj.matrix_world @ v.co for v in bm.verts]

            min_z = min(v.z for v in world_verts)
            max_z = max(v.z for v in world_verts)

            if max_z == min_z:
                z_range = 1
            else:
                z_range = max_z - min_z

            for face in bm.faces:
                for loop in face.loops:
                    vert_index = loop.vert.index
                    z_pos = world_verts[vert_index].z
                    gradient_value = (z_pos - min_z) / z_range
                    color = (gradient_value, gradient_value, gradient_value, 1)
                    
                    loop[color_layer] = get_masked_color((0,0,0,0), color, global_color_settings.get_mask())
            

            bm.to_mesh(mesh)
            bm.free()
            
            obj.data.update()
            
            self.report({"INFO"}, "Vertex colors assigned successfully")

        return {"FINISHED"}
