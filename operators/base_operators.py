import bpy
from bpy.types import Operator

class BaseOperator(Operator):
    bl_label = ""


class BaseColorOperator(BaseOperator):
    """Base operator for verex color operations. Contains a poll method, that prevents using the operator, when no mesh is selected"""

    @classmethod
    def poll(cls, context):
        return len(context.selected_objects) > 0 and bpy.context.object.mode == "OBJECT"
    

