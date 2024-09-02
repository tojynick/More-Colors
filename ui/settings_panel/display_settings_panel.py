from bpy.types import Panel
from ..base_panel_info import BasePanelInfo

class MORECOLORS_PT_display_settings_panel(BasePanelInfo, Panel):
    bl_label = "Display Settings"
    bl_idname = "MORECOLORS_PT_display_settings_panel"
    bl_parent_id = "MORECOLORS_PT_settings_panel"

    def draw(self, context):
        layout = self.layout

        if context.object and context.object.type == "MESH":
            row = layout.row()
            if context.object.mode != "VERTEX_PAINT":
                row.operator("morecolors.enable_vertex_paint_mode", icon = "VPAINT_HLT")
            else:
                row.operator("morecolors.enable_object_mode", icon = "OBJECT_DATAMODE")

            if context.object.mode != "VERTEX_PAINT":
                row = layout.row()
                if context.space_data.shading.color_type != "VERTEX":
                    row.operator("morecolors.show_vertex_colors", icon = "HIDE_ON")
                else:
                    row.operator("morecolors.hide_vertex_colors", icon = "HIDE_OFF")

        elif context.object:
            row = layout.row()
            row.label(text = "Active object is not mesh!", icon = "ERROR")

        else:
            row = layout.row()
            row.label(text = "No active object!", icon = "ERROR")