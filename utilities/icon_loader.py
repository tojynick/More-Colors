import bpy
import bpy.utils.previews
import os

class IconsLoader():
    icons_to_register = {
        "MORE_COLORS_LOGO": ".\Resources\Icon.png"
    }

    @classmethod
    def register_custom_icons(self):
        for icon_id in self.icons_to_register:
            icon_path = self.icons_to_register[icon_id]

            if os.path.exists(icon_path):
                print(icon_path)
                bpy.types.Scene.preview_collection.load(icon_id, os.path.join(os.path.dirname(__file__), "." + icon_path), "IMAGE")
            else:
                print(f"Error: Icon file not found at {icon_path}")
                continue
