import random
import colorsys

def get_random_color_by_RGBA():
    return (random.random(), random.random(), random.random(), random.random())


def get_random_color_by_hue():
    hue = random.random()
    saturation = 1
    lightness = 0.5
    
    r, g, b = colorsys.hls_to_rgb(hue, lightness, saturation)
    
    return (r, g, b, 1)


def get_random_color(mode = "RGBA"):
    match mode:
        case "RGBA":
            return get_random_color_by_RGBA()
        case "Hue":
            return get_random_color_by_hue()


def get_masked_color(old_color, new_color, mask = (True, True, True, True)):
    """Applies new_color to old_color using mask and then returns the result."""

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