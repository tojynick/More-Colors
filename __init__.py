bl_info = {
    "name": "More Colors!",
    "author": "tojynick",
    "description": "A set of tools to make vertex painting easier.",
    "blender": (3, 1, 0),
    "version": (1, 0, 0),
    "location": "3D View > Sidebar > More Colors!",
    "tracker_url": "https://github.com/tojynick/More-Colors",
    "support": "COMMUNITY",
    "category": "Paint"
}

import bpy
from . import operators, ui, property_groups
from .utilities.icon_loader import IconsLoader

packages = [operators, ui, property_groups]

def register():
    for package in packages:
        package.register()

    # Register icons    
    bpy.types.Scene.preview_collection = bpy.utils.previews.new()
    IconsLoader.register_custom_icons()


def unregister():
    for package in packages:
        package.unregister()

    # Unregister icons
    bpy.utils.previews.remove(bpy.types.Scene.preview_collection)
    del bpy.types.Scene.preview_collection
