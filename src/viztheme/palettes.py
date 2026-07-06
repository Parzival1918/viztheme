from matplotlib import cycler


palettes = {
    "pastel": cycler("color", ["#77AADD", "#EE8866", "#EEDD88", "#FFAABB", "#99DDFF", "#44BB99", "#BBCC33"]),
    "okabe_ito": cycler("color", ["#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7"]),
    "purple_yellow": cycler("color", ["#5D3A9B", "#E6C229", "#9E7BCE", "#D1A908", "#351A61", "#F1D873"]),
    "orange_blue": cycler("color", ["#005ABB", "#E36900", "#5D99D4", "#FF9B42", "#002855", "#A84A00"]),
    "neon": cycler("color", ["#00E5FF", "#FF4081", "#FFEA00", "#1DE9B6", "#BB86FC", "#FF6E40"]),
    "grayscale": cycler("color", ["#000000", "#666666", "#252525", "#737373", "#969696", "#BDBDBD", "#D9D9D9"]) 
}


def _linspace(start, stop, n):
    """Yield n evenly spaced values between start and stop (inclusive)."""
    if n == 1:
        yield stop
        return
    h = (stop - start) / (n - 1)
    for i in range(n):
        yield start + h * i


def grayscale_palette(n):
    """Generate a grayscale palette of n colors."""
    return cycler("color", ["#%02x%02x%02x" % (int(i), int(i), int(i)) for i in _linspace(0, 255, n)])
