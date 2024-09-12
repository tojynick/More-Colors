from ..utilities.color_utilities import get_masked_color
from bpy.types import Operator
import bpy
import bmesh

import copy


class MORECOLORS_OT_simple_fill(bpy.types.Operator):
    bl_label = "Apply"
    bl_idname = "morecolors.simple_fill"

    @classmethod
    def poll(cls, context):
        return len(context.selected_objects) > 0
    
    def execute(self, context):
        if not context.selected_objects:
            self.report({"ERROR"}, "No objects selected!")
            return {"CANCELLED"}
        
        scene = context.scene
        global_color_settings = scene.more_colors_global_color_settings
        simple_fill_tool = scene.more_colors_simple_fill_tool

        for obj in context.selected_objects:
            if obj.type != "MESH":
                continue
            
            # We meed tp change mode to object in order to apply vertex colors
            was_in_edit_mode = (obj.mode == "EDIT")
            if was_in_edit_mode:
                bpy.ops.object.mode_set(mode = "OBJECT")

            mesh = obj.data
            
            if not mesh.vertex_colors:
                mesh.vertex_colors.new(name = "Attribute")

            bm = bmesh.new()
            bm.from_mesh(mesh)
            color_layer = bm.loops.layers.color.active

            selected_mode = context.tool_settings.mesh_select_mode

            if was_in_edit_mode:
                bm.faces.ensure_lookup_table()
                bm.verts.ensure_lookup_table()
                bm.edges.ensure_lookup_table()
                
                 # Vertex select mode
                if selected_mode[0]: 
                    selected_loops = [
                        loop for vert in bm.verts if vert.select
                        for loop in vert.link_loops
                    ]
                
                # Edge select mode
                elif selected_mode[1]:  
                    selected_loops = [
                        loop for edge in bm.edges if edge.select
                        for loop in edge.link_loops
                    ]

                # Face select mode
                elif selected_mode[2]:  
                    selected_loops = [
                        loop for face in bm.faces if face.select
                        for loop in face.loops
                    ]

            # If was in object mode
            else:
                selected_loops = [loop for face in bm.faces for loop in face.loops]

            for loop in selected_loops:
                color = simple_fill_tool.selected_color
                loop[color_layer] = get_masked_color((0, 0, 0, 0), color, global_color_settings.get_mask())

            bm.to_mesh(mesh)
            bm.free()

            obj.data.update()

            if was_in_edit_mode:
                bpy.ops.object.mode_set(mode = "EDIT")

        self.report({"INFO"}, "Vertex colors assigned successfully!")
        return {"FINISHED"}
    

class MORECOLORS_OT_select_preset_color(bpy.types.Operator):
    bl_label = "Select"
    bl_idname = "morecolors.select_preset_color"

    preset_name: bpy.props.StringProperty(options = {"HIDDEN"})
    
    def execute(self, context):
        scene = context.scene
        simple_fill_tool = scene.more_colors_simple_fill_tool

        simple_fill_tool.selected_color = getattr(simple_fill_tool, self.preset_name)

        return {"FINISHED"}
    

class MORECOLORS_OT_apply_preset_color(bpy.types.Operator):
    bl_label = "Quick Apply"
    bl_idname = "morecolors.apply_preset_color"

    preset_name: bpy.props.StringProperty(options = {"HIDDEN"})

    @classmethod
    def poll(cls, context):
        return len(context.selected_objects) > 0
    
    def execute(self, context):
        scene = context.scene
        simple_fill_tool = scene.more_colors_simple_fill_tool

        # Copy the color data, instead of creating a reference
        previous_selected_color = list(simple_fill_tool.selected_color)

        simple_fill_tool.selected_color = getattr(simple_fill_tool, self.preset_name)

        bpy.ops.morecolors.simple_fill()

        simple_fill_tool.selected_color = previous_selected_color

        return {"FINISHED"}
