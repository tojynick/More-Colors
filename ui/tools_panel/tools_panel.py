from bpy.types import Panel
from ..base_panel_info import BasePanelInfo

class MORECOLORS_PT_tools_panel(BasePanelInfo, Panel):
    bl_label = "Tools"
    bl_idname = "MORECOLORS_PT_tools_panel"

    def draw(self, context):
        pass