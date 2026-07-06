# Base configuration shared across themes
_base = {
    "lines.linewidth": 2.5,
    "lines.solid_capstyle": "round",
    "lines.solid_joinstyle": "round",
    "axes.grid": True,
    "grid.linestyle": "-",
    "grid.linewidth": 1.0,
    "axes.axisbelow": True,
    "legend.frameon": True,
    "legend.fancybox": True,
    "legend.shadow": False,
    "font.family": "sans-serif",
    "font.sans-serif": ["Segoe UI", "Helvetica Neue", "Arial", "sans-serif"],
}

themes = {
    "light": {
        **_base,
        "figure.facecolor": "#FFFFFF",
        "axes.facecolor": "#F8F9FA",
        "axes.edgecolor": "#333333",
        "text.color": "#333333",
        "grid.color": "#E0E0E0",
    },
    "dark": {
        **_base,
        "figure.facecolor": "#121212",
        "axes.facecolor": "#121212",
        "axes.edgecolor": "#555555",
        "text.color": "#E0E0E0",
        "grid.color": "#2A2A2A",
    }
}
