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
    "xtick.major.pad": 8,
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
    "text.usetex": True,
}

# mpl.rcParams["text.latex.preamble"] = [r"\usepackage{amsmath}"]  # for \text command

mpl.rcParams.update(params)

data = np.loadtxt(paths.data / "ripple_phenomD_matches.txt")
exactmatch_indices = (1.0 - data[:, -1]) <= 0.0
other_indices = (1.0 - data[:, -1]) > 0.0

q = data[:, 1] / data[:, 0]
chieff = (data[:, 0] * data[:, 2] + data[:, 1] * data[:, 3]) / (data[:, 0] + data[:, 1])
Mtot = data[:, 1] + data[:, 0]

# Plot and save
plt.figure(figsize=(7, 5))
cm = plt.cm.get_cmap("inferno")
sc = plt.scatter(
    Mtot[other_indices],
    chieff[other_indices],
    c=np.log10(1.0 - data[other_indices, -1]),
    cmap=cm,
)
plt.colorbar(sc, label=r"$\log_{10}(1-\mathrm{Match})$")

plt.scatter(Mtot[exactmatch_indices], chieff[exactmatch_indices], color="C0")
# plt.xlabel(r"Total Mass, $M$")
# plt.ylabel(r"Mass Ratio, $q$")
plt.xlabel(r"Total Mass, $M$")
plt.ylabel(r"Effective Spin, $\chi_{\rm eff}$")
# plt.xlim(1, 50)
# plt.ylim(1, 50)

plt.savefig(paths.figures / "random_matches.pdf", bbox_inches="tight")
