import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import paths
import arviz as az

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

data_HMC = np.load(paths.data / "chains_HMC.npz")
data_gaussian = np.load(paths.data / "chains_gaussian.npz")

HMC_bestchain = data_HMC["chains"][np.argmax(data_HMC["log_prob"][:, -1])]
gaussian_bestchain = data_gaussian["chains"][
    np.argmax(data_gaussian["log_prob"][:, -1])
]

acl_HMC = az.autocorr(HMC_bestchain.T).T
acl_gaussian = az.autocorr(gaussian_bestchain.T).T

plt.plot(acl_HMC[:, 0], label="HMC")
plt.plot(acl_gaussian[:, 0], label="GRW")
plt.xlim(0, 1000)
plt.ylim(-0.1, 1.0)
plt.xlabel("Lag")
plt.ylabel("Autocorrelation")
plt.legend()
plt.savefig(paths.figures / "autocorrelation.pdf", bbox_inches="tight")
