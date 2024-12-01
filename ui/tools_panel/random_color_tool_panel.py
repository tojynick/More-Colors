from bpy.types import Panel
from ..base_panel_info import BasePanelInfo
from ...utilities.color_utilities import get_active_color_attribute

class MORECOLORS_PT_random_color_tool_panel(BasePanelInfo, Panel):
    bl_label = "Random Color Per Element"
    bl_idname = "MORECOLORS_PT_random_color_tool_panel"
    bl_parent_id = "MORECOLORS_PT_tools_panel"
    bl_options = {"DEFAULT_CLOSED"}
    bl_order = 1

    def draw(self, context):
        layout = self.layout
        
        random_color_tool = context.scene.more_colors_random_color_tool

        show_element_type = True
        obj = context.active_object

        if obj is not None:
            color_attribute = obj.data.color_attributes.active_color

            if color_attribute is not None:
                if color_attribute.domain == "POINT":
                    show_element_type = False

        if show_element_type:
            row = layout.row()
            row.label(text = "Applies a random vertex color per selected element.")

            row = layout.row()
            row.prop(random_color_tool, "element_type")
        
        else:
            row = layout.row()
            row.label(text = "Applies a random vertex color per each point.")

            row = layout.row()
            row.label(text = "If you want to select the element you're applying a random color to, select a color attribute with a \"Face Corner\" domain!", icon = "INFO")

        row = layout.row()
        row.label(text = "Color Generation Method:")
        row.prop(random_color_tool, "color_mode", expand = True)

        row = layout.row()
        row.operator("morecolors.add_random_color", icon = "SHADERFX")
