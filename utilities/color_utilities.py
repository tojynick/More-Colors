import random
import colorsys
import bpy

def get_random_color_by_RGBA():
    """Returns a tuple with 4 floats (RGBA), each float is a random between 0 and 1."""
    return (random.random(), random.random(), random.random(), random.random())


def get_random_color_by_hue():
    """
    Generates a random color in HSL space, with hue being a random number between 0 and 1, saturation being 1, and lightness being 0.5.
    Then, it converts from HSL to RGB space, returning as a float tuple with 4 components (RGBA), where alpha is a random float between 0 and 1.
    """
    hue = random.random()
    saturation = 1
    lightness = 0.5
    
    r, g, b = colorsys.hls_to_rgb(hue, lightness, saturation)
    
    return (r, g, b, random.random())


def get_random_color(mode = "RGBA"):
    """
    Returns a tuple with 4 floats (RGBA). The mode argument controls the color generation algorithm. You can choose between RGBA and Hue modes.
    """

    match mode:
        case "RGBA":
            return get_random_color_by_RGBA()
        case "Hue":
            return get_random_color_by_hue()
        case "Palette":
            return get_color_from_palette()


def get_masked_color(old_color, new_color, mask = (True, True, True, True)):
    """
    Applies new_color to old_color using the mask and then returns the result.
    """

    # Ensure that old_color and new_color are tuples/lists with 4 values (R, G, B, A)
    result_color = [old_color[0], old_color[1], old_color[2], old_color[3]]

    # Apply mask to each channel
    if mask[0]:  # R channel
        result_color[0] = new_color[0]
    if mask[1]:  # G channel
        result_color[1] = new_color[1]
    if mask[2]:  # B channel
        result_color[2] = new_color[2]
    if mask[3]:  # A channel
        result_color[3] = new_color[3]

    return result_color


def get_active_color_attribute(obj):
    """
    Gets an active color attribute of the provided object.
    If there are no color attributes on the object, the default one will be created.
    """

    color_attribute = obj.data.color_attributes.active_color

    # Create a default color attribute layer if there are none
    if color_attribute is None:
        color_attribute = obj.data.color_attributes.new(name = "Color", type = "FLOAT_COLOR", domain = "CORNER")

    return color_attribute


def get_color_from_palette():
    """
    Randomly selects a color from a 4-color palette. The palette is defined in random_color_tool_properties.py
    """
    scene = bpy.context.scene
    random_color_tool = scene.more_colors_random_color_tool

    palette = [random_color_tool.palette_color_1, random_color_tool.palette_color_2, random_color_tool.palette_color_3, random_color_tool.palette_color_4]
    palette_color_id = random.randint(0, len(palette) - 1)

    return palette[palette_color_id]