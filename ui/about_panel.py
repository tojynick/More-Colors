from bpy.types import Panel
from .base_panel_info import BasePanelInfo

class MORECOLORS_PT_about_panel(BasePanelInfo, Panel):
    bl_label = "About"
    bl_idname = "MORECOLORS_PT_about_panel"

    def draw(self, context):
        layout = self.layout

        row = layout.row(align = True)        
        row.label(text = "More Colors! v1.0.1")

        row = layout.row()
        row.label(text = "Made with love by Kai Fardreamer", icon = "FUND")
        
        row = layout.row()
        row.operator("MORECOLORS_OT_open_documentation", icon = "HELP")
