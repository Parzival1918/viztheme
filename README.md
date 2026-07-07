# 🎨 viztheme

`viztheme` is a modern, premium styling package for Matplotlib that makes your scientific plots, business charts, and presentations look stunning, cohesive, and publication-ready out of the box.

---

## ✨ Features

- **Modern Typography & Spacing**: Clean layout defaults with high-quality font fallbacks (`Segoe UI`, `Helvetica Neue`, `Arial`) and elegant padding.
- **Sleek Line Aesthetics**: Thick lines with rounded end-caps and smooth corners for organic, modern shapes.
- **Curated Color Palettes**: Built-in harmonic palettes, including the colorblind-friendly `okabe_ito`, high-contrast `neon`, and custom dynamic `grayscale`.
- **Light & Dark Themes**: Hand-crafted themes optimized for standard displays and large-format projections (posters/presentations).
- **Aesthetic Tweaks**: Easy-to-use utility functions for adding rounded background containers or professional editorial title headings.

---

## 🚀 Installation

You can install `viztheme` directly from the source directory.

### Using `pip`

```bash
pip install .
```

For development mode (editable installation):

```bash
pip install -e .
```

### Using `pixi`

`viztheme` is fully configured with Pixi:

```bash
pixi add --path . viztheme
```

---

## 📖 Quick Start

Using `viztheme` is incredibly simple. Just import the package and call `set_style()` before creating your plots:

```python
import matplotlib.pyplot as plt
import numpy as np
import viztheme

# Apply the global theme, palette, and DPI targets
viztheme.set_style(theme="light", palette="okabe_ito", save_dpi="publication")

# Create a sample plot
x = np.linspace(0, 10, 100)
plt.figure(figsize=(6, 4))
plt.plot(x, np.sin(x), label="Sine wave")
plt.plot(x, np.cos(x), label="Cosine wave")

plt.title("Trigonometric Functions")
plt.xlabel("x value")
plt.ylabel("y value")
plt.legend()

plt.show()
```

---

## 🎨 Themes & Palettes

### Available Themes

Pass these to the `theme` parameter in `set_style()`:

*   `light`: Subtle off-white plotting area with clean gridlines (ideal for documents and web pages).
*   `dark`: Modern, dark-mode styling with high contrast and dark gray background.
*   `poster_light`: Ultra-bold line styles and massive fonts optimized for printed posters or bright presentation slides.
*   `poster_dark`: Ultra-bold line styles and massive fonts styled in dark mode for projectors or screens.

### Available Color Palettes

Pass these to the `palette` parameter in `set_style()`:
*   `okabe_ito` (Default): A colorblind-friendly selection of 8 highly distinguishable colors.
*   `pastel`: Soft, friendly tones for creative or non-technical plots.
*   `purple_yellow`: Sleek combination of rich violets and bright ambers.
*   `orange_blue`: A strong contrasting pair of deep blues and warm oranges.
*   `neon`: Cyberpunk-inspired neon colors for dark-themed visualizations.
*   `grayscale`: Professional neutral shades ranging from black to light gray.

#### Custom Grayscale Palette

You can also generate a custom grayscale palette of any length using `grayscale_palette(n)`:

```python
from viztheme.palettes import grayscale_palette
custom_gray_cycler = grayscale_palette(5)  # Returns a cycler with 5 gray colors
```

---

## 🛠️ Layout Tweaks

`viztheme` includes utility functions in the `tweaks` module to customize the appearance of your plots. These utilities allow you to modify the look of your plots without having to change the default settings.

---

## 🖼️ Gallery Generation

To preview all permutations of themes and palettes, you can build the interactive style gallery.

1. Generate the gallery assets and HTML:
   ```bash
   pixi run python docs/build_gallery.py
   ```
2. Open [docs/index.html](viztheme.naujordep.com) in your web browser to browse through the interactive tabs showcasing all styles and tweaks.

## 📝 License

This project is licensed under the GNU General Public License v3 (GPL v3) - see the [LICENSE](file:///Users/parzival1918/projects/viztheme/LICENSE) file for details.

Author: **Pedro Juan Royo** ([pedro.juan.royo@gmail.com](mailto:pedro.juan.royo@gmail.com))

