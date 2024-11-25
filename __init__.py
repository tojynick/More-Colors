bl_info = {
    "name": "More Colors!",
    "author": "tojynick",
    "description": "A set of tools to make vertex painting easier.",
    "blender": (4, 2, 0),
    "version": (1, 1, 0),
    "location": "3D View > Sidebar > More Colors!",
    "tracker_url": "https://github.com/tojynick/More-Colors",
    "support": "COMMUNITY",
    "category": "Paint"
}

from . import operators, ui, property_groups

# Each package has a register and unregister functions defined in their own __init__.py files
packages = [operators, ui, property_groups]


def register():
    for package in packages:
        package.register()

def unregister():
    for package in packages:
        package.unregister()