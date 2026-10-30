"""Example: crystal mass over 31 days for two seeds (illustrative numbers), in both themes."""
import sys, numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from cc_colors import tokens

day = np.arange(0, 32)
rng = np.random.default_rng(3)
seed_a = 0.6 * (1 + day) ** 1.35 + rng.normal(0, 0.6, day.size)          # g, example
seed_b = 0.6 * (1 + day) ** 1.22 + rng.normal(0, 0.6, day.size)
seed_a[0] = seed_b[0] = 0.6

for theme in ("dark", "light"):
    T = tokens(theme)
    plt.style.use(f"citriccycle-{theme}.mplstyle")
    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.plot(day, seed_a, color=T["series"][0], label="seed A · 24.0 °C")
    ax.plot(day, seed_b, color=T["series"][1], label="seed B · 22.5 °C")
    for y, c, name in ((seed_a, T["series"][0], "A"), (seed_b, T["series"][1], "B")):
        ax.plot(day[-1], y[-1], "o", color=c, markersize=8, markeredgecolor=T["bg"], markeredgewidth=1.5)
        ax.annotate(f"{y[-1]:.1f} g", (day[-1], y[-1]), xytext=(8, 0), textcoords="offset points", va="center", color=T["fg"], fontsize=9.5)
    ax.axvspan(12, 14, color=T["lemon"], alpha=0.18, lw=0)
    ax.text(13, ax.get_ylim()[1] * 0.96, "filter change", ha="center", va="top", color=T["muted"], fontsize=9)
    ax.set_title("0x03 · crystal mass over 31 days (example data)", pad=12)
    ax.set_xlabel("day")
    ax.set_ylabel("mass / g")
    ax.set_xlim(0, 36)
    ax.legend(loc="upper left")
    fig.text(0.01, 0.01, "Citric Cycle · CC BY-NC 4.0 · illustrative numbers, not a measurement", color=T["muted"], fontsize=8)
    fig.tight_layout()
    fig.savefig(f"example-{theme}.png")
    plt.close(fig)
print("ok")
