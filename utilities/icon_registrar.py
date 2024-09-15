import bpy
import bpy.utils.previews
import os

class IconsRegistrar():

    icons_to_register = {
        "MORE_COLORS_LOGO": "resources\icon.png"
    }

    @classmethod
    def register_custom_icons(self):
        for icon_id in self.icons_to_register:
            icon_path = self.icons_to_register[icon_id]
            final_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), icon_path)

            if os.path.exists(final_path):
                bpy.types.Scene.preview_collection.load(icon_id, final_path, "IMAGE")
            else:
                continue
