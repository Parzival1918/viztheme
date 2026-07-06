import matplotlib.pyplot as plt
from typing import Literal
from .styles import themes
from .palettes import palettes


def set_style(theme: str = "light", palette: str = "okabe_ito", save_dpi: int | Literal["small", "medium", "large", "publication"] = "publication"):
    """
    Applies the custom theme and color palette globally.
    """
    if theme not in themes:
        raise ValueError(f"Theme '{theme}' not found. Choose from {list(themes.keys())}")
    if palette not in palettes:
        raise ValueError(f"Palette '{palette}' not found. Choose from {list(palettes.keys())}")

    # Combine the theme dictionary with the chosen palette
    full_style = themes[theme].copy()
    full_style["axes.prop_cycle"] = palettes[palette]
    if save_dpi == "small":
        full_style["savefig.dpi"] = 100
    elif save_dpi == "medium":
        full_style["savefig.dpi"] = 180
    elif save_dpi == "large":
        full_style["savefig.dpi"] = 220
    elif save_dpi == "publication":
        full_style["savefig.dpi"] = 300
    else:
        full_style["savefig.dpi"] = save_dpi

    # Apply it globally
    plt.rcParams.update(full_style)
