import viztheme
import viztheme.tweaks
from pathlib import Path
import shutil
import matplotlib.pyplot as plt
import numpy as np
import inspect


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
    <title>viztheme Gallery</title>
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
    <h1>viztheme Style Gallery</h1>
"""

html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>VizTheme Documentation & Gallery</title>
    <style>
        body { font-family: 'Segoe UI', sans-serif; background: #f0f2f5; color: #1a1a1a; padding: 2rem; max-width: 1200px; margin: 0 auto; }
        
        /* Docs Section Styling */
        .docs-section { background: white; padding: 2.5rem; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); margin-bottom: 2.5rem; }
        .docs-section h2 { border-bottom: 2px solid #f0f2f5; padding-bottom: 0.5rem; margin-top: 0; }
        .tweak-block { margin-top: 2rem; }
        code { background: #f4f4f4; padding: 0.2rem 0.4rem; border-radius: 4px; font-family: 'Courier New', monospace; color: #d63384; font-size: 0.95em; }
        pre code { background: none; color: #e8e8e8; padding: 0; }
        pre { background: #1e1e1e; padding: 1rem; border-radius: 6px; overflow-x: auto; margin-top: 0.5rem; }
        
        /* Gallery & Grid Styling */
        .gallery-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(500px, 1fr)); gap: 2rem; }
        .card { background: white; padding: 1rem; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); border: 1px solid #eee; }
        .card h3 { margin-top: 0; font-size: 1.1rem; border-bottom: 1px solid #eee; padding-bottom: 0.5rem; text-transform: capitalize; }
        img { width: 100%; height: auto; display: block; border-radius: 4px; }
        .card-dark { background: #121212; color: #E0E0E0; }
        .card-dark h3 { border-bottom: 1px solid #2A2A2A; }
        
        /* --- NEW: Tab Styling --- */
        .tab-container { background: white; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); overflow: hidden; margin-bottom: 2rem;}
        .tab { display: flex; background-color: #e9ecef; border-bottom: 1px solid #dee2e6; }
        .tab button { background-color: inherit; flex: 1; border: none; outline: none; cursor: pointer; padding: 1rem; transition: 0.3s; font-size: 1.1rem; font-weight: bold; color: #495057; }
        .tab button:hover { background-color: #dde0e3; }
        .tab button.active { background-color: white; color: #0072B2; border-bottom: 3px solid #0072B2; }
        .tabcontent { display: none; padding: 2rem; animation: fadeEffect 0.5s; }
        
        /* Fade in tabs */
        @keyframes fadeEffect { from {opacity: 0;} to {opacity: 1;} }
    </style>
</head>
<body>
    <h1>VizTheme Package Documentation</h1>

    <h2>🎨 Theme & Palette Gallery</h2>
    <div class="tab-container">
        <div class="tab">
"""

# 3. Generate dummy data once
np.random.seed(42)
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(x + np.pi*3 / 4)

bar_data = [4, 8, 12, 6]
bar_names = ["Low", "Medium", "High", "Extreme"]

for i, theme in enumerate(viztheme.themes.keys()):
    # Make the first tab the default open one
    active_id = 'id="defaultOpen"' if i == 0 else ''
    html += f'<button class="tablinks" onclick="openTheme(event, \'{theme}\')" {active_id}>{theme} theme</button>\n'

html += '</div>\n\n' # Close .tab div

for theme in viztheme.themes.keys():
    html += f'<div id="{theme}" class="tabcontent">\n'
    html += '    <div class="gallery-grid">\n'
    for palette in viztheme.palettes.keys():
        print(f"Generating {theme} - {palette}...")
        
        # Apply the style
        viztheme.set_style(theme=theme, palette=palette)
        
        # Create the plot
        fig = plt.figure(figsize=(10,10))

        gs = fig.add_gridspec(2,2)
        ax1 = fig.add_subplot(gs[0, 0])
        ax2 = fig.add_subplot(gs[0, 1])
        ax3 = fig.add_subplot(gs[1, :])

        ax1.plot(x, y1, label=r"$\sin(x)$")
        ax1.plot(x, y2, label=r"$\cos(x)$")
        ax1.plot(x, y3, label=r"$\sin(x + \pi/4)$")
        ax1.set_title("Plot")
        ax1.set_xlabel("x-axis")
        ax1.set_ylabel("y-axis")
        ax1.legend()

        colors = viztheme.palettes[palette].by_key()["color"]
        ax2.bar(bar_names, bar_data, color=colors[:len(bar_names)])
        ax2.set_title("Bar Chart")
        ax2.set_xlabel("x-axis")
        ax2.set_ylabel("y-axis")

        for i in range(5):
            ax3.scatter(np.random.rand(20) * 10, np.random.rand(20) * 10, s=np.random.rand(20) * 100, alpha=0.6, label=f"Cluster {i}")
        ax3.set_title("Scatter Plot")
        ax3.set_xlabel("x-axis")
        ax3.set_ylabel("y-axis")
        ax3.legend()
        
        # Save as SVG for crisp web rendering
        filename = f"{theme}_{palette}.svg"
        filepath = images_dir / filename
        plt.savefig(filepath, format="svg", bbox_inches="tight")
        plt.close(fig)
        
        # Inject into HTML
        card_class = "card card-dark" if "dark" in theme else "card"
        html += f"""
            <div class="{card_class}">
                <h3>{palette}</h3>
                <img src="images/{filename}" alt="{theme} {palette} plot">
            </div>
        """
        
    html += '    </div>\n'
    html += '</div>\n\n'

html += """
    </div>
"""

tweaks_html = """
    <div class="docs-section">
        <h2>🛠️ Available Tweaks</h2>
        <p>Beyond global styles, <code>viztheme</code> provides these helper functions to elevate your plot aesthetics in the <code>tweaks</code> module.</p>
"""

# Dynamically get tweak functions
tweak_funcs = [f for name, f in inspect.getmembers(viztheme.tweaks, inspect.isfunction) if not name.startswith('_')]

for i, func in enumerate(tweak_funcs, 1):
    name = func.__name__
    title = name.replace('_', ' ').title()
    sig = inspect.signature(func)
    doc = inspect.getdoc(func) or "No description available."
    
    tweaks_html += f"""
        <div class="tweak-block">
            <h3>{i}. {title}</h3>
            <p><code>{name}{sig}</code></p>
            <p>{doc}</p>
        </div>
"""

tweaks_html += """
    </div>
"""

html += tweaks_html
html += """
    <script>
    function openTheme(evt, themeName) {
        var i, tabcontent, tablinks;
        
        // Hide all tab content
        tabcontent = document.getElementsByClassName("tabcontent");
        for (i = 0; i < tabcontent.length; i++) {
            tabcontent[i].style.display = "none";
        }
        
        // Remove 'active' class from all buttons
        tablinks = document.getElementsByClassName("tablinks");
        for (i = 0; i < tablinks.length; i++) {
            tablinks[i].className = tablinks[i].className.replace(" active", "");
        }
        
        // Show the current tab, and add an "active" class to the button that opened the tab
        document.getElementById(themeName).style.display = "block";
        evt.currentTarget.className += " active";
    }

    // Get the element with id="defaultOpen" and click on it to open the first tab on page load
    document.getElementById("defaultOpen").click();
    </script>
</body>
</html>
"""

with open(Path(__file__).parent / "index.html", "w") as f:
    f.write(html)

print("Gallery built successfully!")