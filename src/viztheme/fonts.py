import os
import matplotlib.font_manager as fm


def load_font(font_path: str):
    """
    Loads a custom font file (TTF/OTF) and registers it with Matplotlib.
    Returns the font name so it can be used in matplotlib config.
    """
    if not os.path.exists(font_path):
        raise FileNotFoundError(f"Font file not found: {font_path}")
        
    fm.fontManager.addfont(font_path)
    prop = fm.FontProperties(fname=font_path)
    return prop.get_name()
