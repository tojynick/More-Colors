from .base_operators import BaseColorOperator
import bpy

class MORECOLORS_OT_reset_color(BaseColorOperator):
    """Resets all vertex colors to black"""

    bl_label = "Reset Vertex Colors"
    bl_idname = "morecolors.reset_vertex_colors"
    
    def execute(self, context):
        for obj in context.selected_objects:
            if obj.type != "MESH":
                continue
            
            mesh = obj.data
            
            if not mesh.vertex_colors:
                vertex_colors = mesh.vertex_colors.new(name = "Attribute")
            else:
                vertex_colors = mesh.vertex_colors.active

            for face in mesh.polygons:
                for loop_index in face.loop_indices:
                    vertex_colors.data[loop_index].color = (0,0,0,0)
        
        self.report({"INFO"}, "Vertex colors have been reset!")

        return {"FINISHED"}
