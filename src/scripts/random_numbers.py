import matplotlib.pyplot as plt
import numpy as np
import paths
import matplotlib as mpl

params = {
    "font.size": 18,
    "legend.fontsize": 18,
    "legend.frameon": False,
    "axes.labelsize": 18,
    "axes.titlesize": 18,
    "xtick.labelsize": 18,
    "ytick.labelsize": 18,
    "figure.figsize": (7, 5),
    "xtick.top": True,
    "ytick.right": True,
    "xtick.bottom": True,
    "ytick.left": True,
    "xtick.major.size": 8,
    "xtick.minor.size": 4,
    "ytick.major.size": 8,
    "ytick.minor.size": 4,
    "xtick.direction": "in",
    "ytick.direction": "in",
    "text.usetex": True,
    "font.family": "serif",
    "axes.linewidth": 1.5,
    "mathtext.fontset": "dejavuserif",
}


mpl.rcParams["text.latex.preamble"] = [r"\usepackage{amsmath}"]  # for \text command

mpl.rcParams.update(params)

# Generate some data
random_numbers = np.random.randn(100, 10)

# Plot and save
fig = plt.figure(figsize=(7, 6))
plt.plot(random_numbers)
plt.xlabel("x")
plt.ylabel("y")
fig.savefig(paths.figures / "random_numbers.pdf", bbox_inches="tight", dpi=300)
