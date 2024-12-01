from bpy.types import Panel
from ..base_panel_info import BasePanelInfo

import bpy

class MORECOLORS_PT_color_by_position_tool_panel(BasePanelInfo, Panel):
    bl_label = "Color By Position"
    bl_idname = "MORECOLORS_PT_color_by_position_tool_panel"
    bl_parent_id = "MORECOLORS_PT_tools_panel"
    bl_options = {"DEFAULT_CLOSED"}
    bl_order = 2


    def draw(self, context):
        layout = self.layout

        color_by_position_tool = context.scene.more_colors_color_by_position_tool

        # About the color ramp
        # I didn't find a better way, so my approach is: 
        # 1. Create a material that will store color ramp data
        # 2. Draw this data to the panel
        # 3. Use the data to control the gradient creation later
        #
        # If you know a better way, please contact me!

        # If there is no color ramp material, I ask the user to call an operator that will create the material
        if bpy.data.materials.get(color_by_position_tool.color_ramp_material_name) is None:
            row = layout.row()
            row.operator("morecolors.initialize_color_by_position_tool", icon = "TOOL_SETTINGS")
        
        # Draw the tool
        else:
            row = layout.row()
            row.label(text = "Applies a position-based vertex color.")
            
            row = layout.row()
            row.label(text = "Space Type:")
            row.prop(color_by_position_tool, "space_type", expand = True)

            row = layout.row()
            row.prop(color_by_position_tool, "gradient_direction")

            material = bpy.data.materials.get(color_by_position_tool.color_ramp_material_name)
            node = material.node_tree.nodes['Color Ramp']
            layout.template_color_ramp(node, "color_ramp")

            layout.row()

            row = layout.row()
            row.operator("morecolors.add_color_by_position", icon = "BRUSH_DATA")

            row = layout.row()
            row.operator("morecolors.reset_color_by_position_gradient", icon = "TRASH")