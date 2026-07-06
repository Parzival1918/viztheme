_base_default = {
    "lines.linewidth": 2.5,
    "lines.solid_capstyle": "round",     # Rounds the ends of the lines
    "lines.solid_joinstyle": "round",    # Smooths out the corners where lines bend

    "axes.grid": True,                   # Turns on the major grid
    "grid.color": "#E5E5E5",             # Soft gray grid lines
    "grid.linestyle": "-",
    "grid.linewidth": 1.0,
    "axes.axisbelow": True,              # Ensures grid stays behind the plotted lines

    "legend.frameon": True,
    "legend.fancybox": True,             # Gives the legend box rounded corners
    "legend.shadow": False,              # Adds the shaded drop-shadow effect
    "legend.framealpha": 0.9,           # Slight transparency 
    "legend.edgecolor": "#CCCCCC",

    "font.family": "sans-serif",
    "font.sans-serif": ["Segoe UI", "Helvetica Neue", "Arial", "sans-serif"],
    "font.size": 11,
    "axes.titlesize": 14,
    "axes.labelsize": 12,

    "scatter.marker": "s",

    "figure.dpi": 100,

    "xtick.direction": "in",
    "ytick.direction": "in",

    "savefig.bbox": "tight",
}

_base_poster = {
    "font.family": "sans-serif",
    "font.sans-serif": ["Segoe UI", "Helvetica Neue", "Arial", "sans-serif"],
    "font.size": 18,               # Massive increase to base font size
    "axes.titlesize": 24,          # Huge, bold titles
    "axes.titleweight": "bold",
    "axes.labelsize": 20,          # Large X/Y axis labels
    "xtick.labelsize": 14,         # Readable tick numbers
    "ytick.labelsize": 14,
    "legend.fontsize": 14,
    
    "lines.linewidth": 4.5,              # Thicker lines for projector visibility
    "lines.solid_capstyle": "round",
    "lines.solid_joinstyle": "round",
    "lines.markersize": 12,              # Larger data points on scatter plots

    "axes.linewidth": 2.5,               # Thicker border around the plot
    "xtick.major.width": 2.0,            # Thicker tick marks
    "ytick.major.width": 2.0,
    "xtick.major.size": 8,               # Longer tick marks
    "ytick.major.size": 8,

    "axes.grid": True,
    "grid.color": "#CCCCCC",             # Slightly darker gray so it survives projection
    "grid.linestyle": "-",
    "grid.linewidth": 1.5,               # Thicker grid lines
    "axes.axisbelow": True,

    "legend.frameon": True,
    "legend.fancybox": True,
    "legend.shadow": False,
    "legend.framealpha": 0.9,            # Solid background to block grid lines perfectly
    "legend.edgecolor": "#999999",

    "savefig.bbox": "tight",
}

themes = {
    "light": {
        **_base_default,
        "figure.facecolor": "#FFFFFF",
        "axes.facecolor": "#F8F9FA",
        "axes.edgecolor": "#333333",
        "text.color": "#333333",
        "grid.color": "#E0E0E0",
    },
    "dark": {
        **_base_default,
        "figure.facecolor": "#121212",
        "axes.facecolor": "#121212",
        "axes.edgecolor": "#555555",
        "text.color": "#E0E0E0",
        "axes.titlecolor": "#E0E0E0",
        "axes.labelcolor": "#E0E0E0",
        "xtick.color": "#E0E0E0",
        "ytick.color": "#E0E0E0",
        "grid.color": "#2A2A2A",
    },
    "poster_light": {
        **_base_poster,
        "figure.facecolor": "#FFFFFF",
        "axes.facecolor": "#F8F9FA",
        "axes.edgecolor": "#333333",
        "text.color": "#333333",
        "grid.color": "#E0E0E0",
        "xtick.color": "#333333",
        "ytick.color": "#333333",
        "axes.titlecolor": "#333333",
        "axes.labelcolor": "#333333",
    },
    "poster_dark": {
        **_base_poster,
        "figure.facecolor": "#121212",
        "axes.facecolor": "#121212",
        "axes.edgecolor": "#555555",
        "text.color": "#E0E0E0",
        "axes.titlecolor": "#E0E0E0",
        "axes.labelcolor": "#E0E0E0",
        "xtick.color": "#E0E0E0",
        "ytick.color": "#E0E0E0",
        "grid.color": "#2A2A2A",
    }
}
