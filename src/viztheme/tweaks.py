import matplotlib.patches as patches
import matplotlib.pyplot as plt


def _get_ax(ax=None):
    if ax is None:
        ax = plt.gca()
    return ax


def add_rounded_box(facecolor="#F8F9FA", edgecolor="#CCCCCC", ax=None):
    """Removes standard spines and adds a rounded background box."""
    ax = _get_ax(ax)
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


def format_editorial(title, subtitle, ax=None):
    """Applies a left-aligned editorial title and subtitle."""
    ax = _get_ax(ax)
    ax.set_title(title, loc='left', fontsize=16, fontweight='bold', pad=25)
    ax.text(0, 1.06, subtitle, transform=ax.transAxes, fontsize=11, color='#666666')


def remove_grid(ax=None):
    """Removes the grid of the plot."""
    ax = _get_ax(ax)
    ax.grid(False)


def despine(ax=None, top=True, right=True, left=False, bottom=False):
    """Remove standard spines from plot."""
    ax = _get_ax(ax)
    if top:
        ax.spines['top'].set_visible(False)
    if right:
        ax.spines['right'].set_visible(False)
    if left:
        ax.spines['left'].set_visible(False)
    if bottom:
        ax.spines['bottom'].set_visible(False)


def move_legend_outside(ax=None, loc="center left", bbox_to_anchor=(1.05, 0.5)):
    """Moves the legend outside the axes."""
    ax = _get_ax(ax)
    legend = ax.get_legend()
    if legend is not None:
        ax.legend(loc=loc, bbox_to_anchor=bbox_to_anchor)


def add_watermark(text="Confidential", alpha=0.1, ax=None, fontsize=40, color="gray", rotation=45):
    """Adds a diagonal watermark to the plot."""
    ax = _get_ax(ax)
    ax.text(0.5, 0.5, text, transform=ax.transAxes,
            fontsize=fontsize, color=color, alpha=alpha,
            ha='center', va='center', rotation=rotation)


def label_bars(ax=None, fmt="%g", padding=3, color="black", fontsize=10):
    """Adds labels above/next to bar charts."""
    ax = _get_ax(ax)
    for container in ax.containers:
        ax.bar_label(container, fmt=fmt, padding=padding, color=color, fontsize=fontsize)

