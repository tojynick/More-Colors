from bpy.types import Panel
from ..base_panel_info import BasePanelInfo

class MORECOLORS_PT_display_settings_panel(BasePanelInfo, Panel):
    bl_label = "Display Settings"
    bl_idname = "MORECOLORS_PT_display_settings_panel"
    bl_parent_id = "MORECOLORS_PT_settings_panel"

    def draw(self, context):
        layout = self.layout

        display_settings = context.scene.more_colors_display_settings

        if context.object and context.object.type == "MESH":
            if context.object.mode != "VERTEX_PAINT":
                row = layout.row()
                row.label(text = "Vertex colors display mode:", icon = "MESH_DATA")

                row = layout.row()
                row.prop(display_settings, "display_mode", expand = True)

                row = layout.row()
                row.label(text = "Alpha display mode will temporary override all mesh materials!", icon = "ERROR")

            else:
                row = layout.row()
                row.label(text = "Enter object mode!", icon = "ERROR")

        elif context.object:
            row = layout.row()
            row.label(text = "Active object is not mesh!", icon = "ERROR")

        else:
            row = layout.row()
            row.label(text = "No active object!", icon = "ERROR")
