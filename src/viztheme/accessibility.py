import numpy as np
import matplotlib.pyplot as plt


def simulate_colorblindness(fig=None, mode="protanopia"):
    """
    Simulates how a matplotlib figure looks to someone with colorblindness.
    Supported modes: 'protanopia', 'deuteranopia', 'tritanopia', 'achromatopsia'.
    """
    if fig is None:
        fig = plt.gcf()
        
    # Draw the figure to the canvas to get the pixel data
    fig.canvas.draw()
    
    # Get the RGB buffer from the figure
    buf = np.asarray(fig.canvas.buffer_rgba())
    img = buf[..., :3].astype(float)
    
    # Matrices for colorblindness simulation
    matrices = {
        "protanopia": np.array([[0.56667, 0.43333, 0.0],
                                [0.55833, 0.44167, 0.0],
                                [0.0,     0.24167, 0.75833]]),
        "deuteranopia": np.array([[0.625,   0.375,   0.0],
                                  [0.7,     0.3,     0.0],
                                  [0.0,     0.3,     0.7]]),
        "tritanopia": np.array([[0.95,    0.05,    0.0],
                                [0.0,     0.43333, 0.56667],
                                [0.0,     0.475,   0.525]]),
        "achromatopsia": np.array([[0.299, 0.587, 0.114],
                                   [0.299, 0.587, 0.114],
                                   [0.299, 0.587, 0.114]])
    }
    
    if mode not in matrices:
        raise ValueError(f"Unknown mode '{mode}'. Choose from {list(matrices.keys())}")
        
    matrix = matrices[mode]
    
    # Apply matrix transformation
    simulated = np.dot(img, matrix.T)
    simulated = np.clip(simulated, 0, 255).astype(np.uint8)
    
    # Create a new figure to show the simulated result
    sim_fig, ax = plt.subplots(figsize=(fig.get_figwidth(), fig.get_figheight()), dpi=fig.dpi)
    ax.imshow(simulated)
    ax.axis("off")
    ax.set_title(f"Simulated {mode.capitalize()}")
    
    return sim_fig
