from bpy.types import Operator

class BaseOperator(Operator):
    """Containts basic properties for an operator such as label and REGISTER, UNDO options"""
    bl_label = ""
    bl_options = {"REGISTER", "UNDO"}
