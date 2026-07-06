import matplotlib.patches as patches


def add_rounded_box(ax, facecolor="#F8F9FA", edgecolor="#CCCCCC"):
    """Removes standard spines and adds a rounded background box."""
    for spine in ax.spines.values():
        spine.set_visible(False)
        
    rounded_box = patches.FancyBboxPatch(
        (0, 0), 1, 1,                                   
        transform=ax.transAxes,                         
        boxstyle="round,pad=0.01,rounding_size=0.03",   
        edgecolor=edgecolor,                            
        facecolor=facecolor,                            
        linewidth=1.5,
        zorder=0,                                       
        clip_on=False
    )
    ax.add_patch(rounded_box)


def format_editorial(ax, title, subtitle):
    """Applies a left-aligned editorial title and subtitle."""
    ax.set_title(title, loc='left', fontsize=16, fontweight='bold', pad=25)
    ax.text(0, 1.06, subtitle, transform=ax.transAxes, fontsize=11, color='#666666')
