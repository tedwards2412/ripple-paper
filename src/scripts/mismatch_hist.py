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
    "figure.figsize": (7, 5),
    "xtick.top": True,
    "axes.unicode_minus": False,
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

(catalog_num, ori_loss, opt_loss) = np.loadtxt(
    paths.data / "mismatch_hist.txt", unpack=True
)
bins = np.arange(-5, -1, 0.125)

plt.hist(np.log10(ori_loss), bins=bins, alpha=0.3, color="C0")
plt.hist(np.log10(ori_loss), bins=bins, label="Original", histtype="step", color="C0")
plt.hist(np.log10(opt_loss), bins=bins, alpha=0.3, color="C1")
plt.hist(np.log10(opt_loss), bins=bins, label="Optimized", histtype="step", color="C1")
plt.legend()
plt.xlim(1e-5, 0.1)
plt.xlabel("$\log(\mathcal{M})$")
plt.ylabel("Count")
plt.savefig(paths.figures / "mismatch_hist.pdf", bbox_inches="tight")
