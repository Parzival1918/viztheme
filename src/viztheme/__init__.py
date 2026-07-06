import matplotlib.pyplot as plt
from .styles import themes
from .palettes import palettes


def set_style(theme="light", palette="okabe_ito"):
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

    # Apply it globally
    plt.rcParams.update(full_style)
