from ..base_panel_info import BasePanelInfo
from bpy.types import Panel

class MORECOLORS_PT_global_color_settings_panel(BasePanelInfo, Panel):
    bl_label = "Global Color Settings"
    bl_idname = "MORECOLORS_PT_global_color_settings_panel"
    bl_parent_id = "MORECOLORS_PT_settings_panel"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        tool = scene.more_colors_gloabal_color_settings

        # Global Color Mask
        row = layout.row()
        row.label(text = "Color Mask", icon = "COLOR")

        row = layout.row()
        row.label(text = "Affected color channels:")

        
        row = layout.row(align = True)
        row.prop(tool, "global_color_mask_r", text = "R", toggle = True)
        row.prop(tool, "global_color_mask_g", text = "G", toggle = True)
        row.prop(tool, "global_color_mask_b", text = "B", toggle = True)
        row.prop(tool, "global_color_mask_a", text = "A", toggle = True)
