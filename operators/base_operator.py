from bpy.types import Operator

class BaseOperator(Operator):
    bl_label = ""
    bl_options = {"REGISTER", "UNDO"}