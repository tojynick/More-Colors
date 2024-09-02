from bpy.types import Panel
from ..base_panel_info import BasePanelInfo

class MORECOLORS_PT_random_color_tool_panel(BasePanelInfo, Panel):
    bl_label = "Random Color Per Element"
    bl_idname = "MORECOLORS_PT_random_color_tool_panel"
    bl_parent_id = "MORECOLORS_PT_tools_panel"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout

        tool = context.scene.more_colors_random_color_tool
        
        row = layout.row()
        row.prop(tool, "element_type")

        row = layout.row()
        row.operator("morecolors.add_random_color", icon = "SHADERFX")