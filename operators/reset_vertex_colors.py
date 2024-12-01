from ..utilities.color_utilities import get_active_color_attribute
from .base_operators import BaseColorOperator

class MORECOLORS_OT_reset_color(BaseColorOperator):
    """Resets all vertex colors to white"""

    bl_label = "Reset Vertex Colors"
    bl_idname = "morecolors.reset_vertex_colors"
    
    def execute(self, context):
        for obj in context.selected_objects:
            if obj.type != "MESH":
                continue
            
            color_attribute = get_active_color_attribute(obj)

            for data in color_attribute.data:
                data.color_srgb = (1,1,1,1)
        
        self.report({"INFO"}, "Vertex colors have been reset!")

        return {"FINISHED"}
