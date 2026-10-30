"""Citric Cycle colour helpers for matplotlib: validated categorical order, sequential and diverging ramps, hero/annotation tokens."""
from matplotlib.colors import LinearSegmentedColormap

DARK = dict(bg="#0B2A33", fg="#F4F6F5", muted="#8FB0B8", grid="#1C4A58", lemon="#F9CF3B",
            series=["#A48200", "#0094A2", "#7971D0", "#C3518D"])
LIGHT = dict(bg="#FFFFFF", fg="#0B2A33", muted="#4F6B73", grid="#C9D4D7", lemon="#D9A21B",
             series=["#AF7C00", "#1C96A8", "#5B52C9", "#B8236F"])

# sequential: one hue (teal), light → dark; reverse for dark surfaces so high = bright
cc_teal = LinearSegmentedColormap.from_list("cc_teal", ["#E2F3F6", "#5FC3D3", "#1F6B7A", "#0B2A33"])
cc_teal_dark = LinearSegmentedColormap.from_list("cc_teal_dark", ["#15424E", "#1F6B7A", "#5FC3D3", "#CDEFF4"])
# diverging: cyan ↔ neutral grey ↔ magenta (two hues + grey midpoint)
cc_div = LinearSegmentedColormap.from_list("cc_div", ["#1C96A8", "#B7C4C8", "#B8236F"])
cc_div_dark = LinearSegmentedColormap.from_list("cc_div_dark", ["#5FC3D3", "#52666C", "#F585C0"])


def tokens(theme="dark"):
    return DARK if theme == "dark" else LIGHT
