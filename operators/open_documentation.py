from .base_operators import BaseOperator
import webbrowser


class MORECOLORS_OT_open_documentation(BaseOperator):
    """Opens a github page with documentation."""

    bl_label = "Need help? Read the docs!"
    bl_idname = "morecolors.open_documentation"

    def execute(self, context):
        url = "https://github.com/tojynick/More-Colors"
        webbrowser.open(url)

        return {"FINISHED"}
