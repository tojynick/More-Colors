from bpy.types import Panel
from ..base_panel_info import BasePanelInfo

class MORECOLORS_PT_settings_panel(BasePanelInfo, Panel):
    bl_label = "Settings"
    bl_idname = "MORECOLORS_PT_settings_panel"

    def draw(self, context):
        pass