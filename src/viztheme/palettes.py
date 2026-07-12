from matplotlib import cycler
from matplotlib.colors import LinearSegmentedColormap
import matplotlib.pyplot as plt


palettes = {
    "pastel": cycler("color", ["#77AADD", "#EE8866", "#EEDD88", "#FFAABB", "#99DDFF", "#44BB99", "#BBCC33"]),
    "okabe_ito": cycler("color", ["#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7"]),
    "purple_yellow": cycler("color", ["#5D3A9B", "#E6C229", "#9E7BCE", "#D1A908", "#351A61", "#F1D873"]),
    "orange_blue": cycler("color", ["#005ABB", "#E36900", "#5D99D4", "#FF9B42", "#002855", "#A84A00"]),
    "neon": cycler("color", ["#00E5FF", "#FF4081", "#FFEA00", "#1DE9B6", "#BB86FC", "#FF6E40"]),
    "grayscale": cycler("color", ["#000000", "#666666", "#252525", "#737373", "#969696", "#BDBDBD", "#D9D9D9"]) 
}

colorblind_safe_palettes = ["okabe_ito", "grayscale"]

def get_palettes(colorblind_safe=False):
    if colorblind_safe:
        return {k: v for k, v in palettes.items() if k in colorblind_safe_palettes}
    return palettes

continuous_colormaps = {
    "viztheme_seq_blue": LinearSegmentedColormap.from_list("viztheme_seq_blue", ["#EAF4FF", "#005ABB", "#002855"]),
    "viztheme_seq_orange": LinearSegmentedColormap.from_list("viztheme_seq_orange", ["#FFF1E5", "#FF9B42", "#A84A00"]),
    "viztheme_div_orange_blue": LinearSegmentedColormap.from_list("viztheme_div_orange_blue", ["#E36900", "#F8F9FA", "#005ABB"]),
    "viztheme_div_purple_yellow": LinearSegmentedColormap.from_list("viztheme_div_purple_yellow", ["#5D3A9B", "#F8F9FA", "#E6C229"])
}

def register_colormaps():
    for name, cmap in continuous_colormaps.items():
        if name not in plt.colormaps():
            plt.colormaps.register(cmap=cmap, name=name)


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
