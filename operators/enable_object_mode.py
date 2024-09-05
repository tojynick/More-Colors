from .base_operators import BaseOperator
import bpy

class MORECOLORS_OT_enable_object_mode(BaseOperator):
    bl_label = "Swtitch To Object Mode"
    bl_idname = "morecolors.enable_object_mode"

    def execute(self, context):
        context.space_data.shading.type = "SOLID"
        bpy.ops.object.mode_set(mode = "OBJECT")

        return {"FINISHED"}
