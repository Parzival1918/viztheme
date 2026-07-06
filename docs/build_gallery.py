from pathlib import Path
import shutil
import matplotlib.pyplot as plt
import numpy as np
import viztheme

# 1. Prepare the output directories, delete output image dir first
images_dir = Path(__file__).parent / "images"
if images_dir.exists():
    shutil.rmtree(images_dir)
images_dir.mkdir()

# 2. Setup the HTML template with simple CSS Grid
html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>VizTheme Gallery</title>
    <style>
        body { font-family: 'Segoe UI', sans-serif; background: #f0f2f5; color: #1a1a1a; padding: 2rem; }
        h1 { text-align: center; margin-bottom: 2rem; }
        .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(500px, 1fr)); gap: 2rem; }
        .card { background: white; padding: 1rem; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
        .card h2 { margin-top: 0; font-size: 1.2rem; border-bottom: 1px solid #eee; padding-bottom: 0.5rem;}
        .card-dark { background: #121212; color: #E0E0E0; }
        .card-dark h2 { border-bottom: 1px solid #2A2A2A; }
        img { width: 100%; height: auto; display: block; }
    </style>
</head>
<body>
    <h1>VizTheme Style Gallery</h1>
    <div class="grid">
"""

# 3. Generate dummy data once
np.random.seed(42)
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(x + np.pi*3 / 4)

# 4. Loop through themes and palettes
themes = ["light", "dark"]
palettes = ["pastel", "okabe_ito", "purple_yellow", "neon", "grayscale"]

for theme in themes:
    for palette in palettes:
        print(f"Generating {theme} - {palette}...")
        
        # Apply the style
        viztheme.set_style(theme=theme, palette=palette)
        
        # Create the plot
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.plot(x, y1, label="$\sin(x)$")
        ax.plot(x, y2, label="$\cos(x)$")
        ax.plot(x, y3, label="$\sin(x + \pi/4)$")
        ax.set_title("Title")
        ax.set_xlabel("x-axis")
        ax.set_ylabel("y-axis")
        ax.legend()
        
        # Save as SVG for crisp web rendering
        filename = f"{theme}_{palette}.svg"
        plt.savefig(f"images/{filename}", format="svg", bbox_inches="tight")
        
        # Inject into HTML
        card_class = "card card-dark" if theme == "dark" else "card"
        html += f"""
        <div class="{card_class}">
            <h2>{theme.title()} + {palette.title()}</h2>
            <img src="images/{filename}" alt="{theme} {palette} plot">
        </div>
        """

# 5. Close HTML and write to file
html += """
    </div>
</body>
</html>
"""

with open("index.html", "w") as f:
    f.write(html)

print("Gallery built successfully!")