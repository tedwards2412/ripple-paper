import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import paths

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


mpl.rcParams.update(params)

(freq, ori_error, opt_error) = np.loadtxt(paths.data / "loss_compare.txt", unpack=True)


plt.axvline(x=0.018, color="k", alpha=0.5, ls="--")
# fRD =
# 0.5fRD
plt.axvline(x=0.08, color="k", alpha=0.4, ls="--")
plt.plot(freq, ori_error, label="Original")
plt.plot(freq, opt_error, label="Optimized")
plt.legend()
plt.xlabel(r"$Mf$")
plt.ylabel(r"$\Delta|\tilde{h}(f)|$")
plt.xlim(0.01, 0.1)
plt.savefig(paths.figures / "loss_compare.pdf", bbox_inches="tight")