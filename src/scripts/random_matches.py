import matplotlib.pyplot as plt
import numpy as np
import paths
import matplotlib as mpl
import matplotlib.cm as cm
from matplotlib import colors
from scipy.spatial import Voronoi, voronoi_plot_2d

params = {
    "font.size": 18,
    "legend.fontsize": 18,
    "legend.frameon": False,
    "axes.labelsize": 18,
    "axes.titlesize": 18,
    "xtick.labelsize": 18,
    "ytick.labelsize": 18,
    "axes.unicode_minus": False,
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
    "axes.linewidth": 1.5,
    "text.usetex": False,
    "font.family": "serif",
    "font.serif": "cmr10",
    "mathtext.fontset": "cm",
    "axes.formatter.use_mathtext": True,  # needed when using cm=cmr10 for normal text
}

# mpl.rcParams["text.latex.preamble"] = [r"\usepackage{amsmath}"]  # for \text command

# params = {
#     "font.size": 18,
#     "legend.fontsize": 18,
#     "legend.frameon": False,
#     "axes.labelsize": 18,
#     "axes.titlesize": 18,
#     "xtick.labelsize": 18,
#     "ytick.labelsize": 18,
#     "figure.figsize": (7, 5),
#     "xtick.top": True,
#     "ytick.right": True,
#     "xtick.bottom": True,
#     "ytick.left": True,
#     "xtick.major.pad": 8,
#     "xtick.major.size": 8,
#     "xtick.minor.size": 4,
#     "ytick.major.size": 8,
#     "ytick.minor.size": 4,
#     "xtick.direction": "in",
#     "ytick.direction": "in",
#     "text.usetex": True,
#     "font.family": "serif",
#     "axes.linewidth": 1.5,
#     "mathtext.fontset": "dejavuserif",
#     "text.usetex": True,
# }

# mpl.rcParams["text.latex.preamble"] = [r"\usepackage{amsmath}"]  # for \text command

mpl.rcParams.update(params)

data = np.loadtxt(paths.data / "ripple_phenomD_matches.txt")
data = data[data[:, -1].argsort()]
data = data[::-1]

exactmatch_indices = (1.0 - data[:, -1]) <= 0.0
other_indices = (1.0 - data[:, -1]) > 0.0

q = data[:, 1] / data[:, 0]
chieff = (data[:, 0] * data[:, 2] + data[:, 1] * data[:, 3]) / (data[:, 0] + data[:, 1])
Mtot = data[:, 1] + data[:, 0]

# Plot and save
plt.figure(figsize=(7, 5))
# plt.scatter(Mtot[exactmatch_indices], chieff[exactmatch_indices], color="gray", alpha=0.3)
data[exactmatch_indices, -1] = 1.0 - 1e-16
cm = plt.cm.get_cmap("inferno")
sc = plt.scatter(
    Mtot[:],
    chieff[:],
    c=np.log10(1.0 - data[:, -1]),
    cmap=cm,
    vmin=-16,
    vmax=-12,
    s=20
)
plt.colorbar(sc, label=r"$\log_{10}(1-\mathrm{Match})$")

# thetas = np.array([Mtot,chieff]).T
# vor = Voronoi(thetas)
# norm = colors.Normalize(-16, -12.5)
# cmap = cm.ScalarMappable(norm=norm)
# voronoi_plot_2d(vor, show_vertices=False, line_width=0.1, point_size=0.1)
# for r in range(len(vor.point_region)):
#     region = vor.regions[vor.point_region[r]]
#     if -1 not in region:
#         polygon = [vor.vertices[i] for i in region]
#         plt.fill(*zip(*polygon), color=cmap.to_rgba(np.log10(1.0 - data[r, -1])))

# plt.colorbar(
#     cmap,
#     label=r"Temp",
# )

# plt.xlabel(r"Total Mass, $M$")
# plt.ylabel(r"Mass Ratio, $q$")
plt.xlabel(r"Total Mass, $M$")
plt.ylabel(r"Effective Spin, $\chi_{\rm eff}$")
plt.xlim(0, 200)
plt.ylim(-1, 1.)
# plt.ylim(1, 50)

plt.savefig(paths.figures / "random_matches.pdf", bbox_inches="tight")
