from bpy.types import Panel

class MORECOLORS_PT_main_panel(Panel):
    
    bl_label = "More Colors!"
    bl_idname = "ADDONNAME_PT_main_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "More Colors!"

    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        row.operator("morecolors.add_random_color")