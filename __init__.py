bl_info = {
    "name": "More Colors!",
    "author": "tojynick",
    "description": "A set of tools to make vertex painting easier.",
    "blender": (4, 0, 0),
    "version": (1, 0, 0),
    "location": "",
    "tracker_url": "https://github.com/tojynick/More-Colors",
    "support": "COMMUNITY",
    "category": "Paint"
}

import bpy
from . import operators, ui

operator_classes = [operators.MORECOLORS_OT_add_random_color]
ui_classes = [ui.MORECOLORS_PT_main_panel]

def register():
    for op_cls in operator_classes:
        bpy.utils.register_class(op_cls)

    for ui_cls in ui_classes:
        bpy.utils.register_class(ui_cls)

def unregister():
    for op_cls in operator_classes:
        bpy.utils.unregister_class(op_cls)
    
    for ui_cls in ui_classes:
        bpy.utils.unregister_class(ui_cls)