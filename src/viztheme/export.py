import matplotlib.pyplot as plt


def save_fig(filename, fig=None, transparent=False, formats=["png", "svg"], dpi=None):
    """
    Saves the figure in multiple formats simultaneously.
    """
    if fig is None:
        fig = plt.gcf()
        
    for fmt in formats:
        if filename.endswith(f".{fmt}"):
            out_name = filename
        else:
            base = filename.rsplit('.', 1)[0] if '.' in filename else filename
            out_name = f"{base}.{fmt}"
            
        fig.savefig(out_name, format=fmt, transparent=transparent, bbox_inches="tight", dpi=dpi)
