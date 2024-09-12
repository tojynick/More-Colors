from bpy.types import Panel
from ..base_panel_info import BasePanelInfo

class MORECOLORS_PT_random_color_tool_panel(BasePanelInfo, Panel):
    bl_label = "Color By Position"
    bl_idname = "MORECOLORS_PT_color_by_position_tool_panel"
    bl_parent_id = "MORECOLORS_PT_tools_panel"
    bl_options = {"DEFAULT_CLOSED"}
    bl_order = 2

    def draw(self, context):
        layout = self.layout

        color_by_position_tool = context.scene.more_colors_color_by_position_tool

        row = layout.row()
        row.label(text = "Applies a position-based vertex color.")
        
        row = layout.row()
        row.label(text = "Space Type:")
        row.prop(color_by_position_tool, "space_type", expand = True)

        row = layout.row()
        row.prop(color_by_position_tool, "gradient_direction")

        row = layout.row()
        row.operator("morecolors.add_color_by_position", icon = "BRUSH_DATA")

