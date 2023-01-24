import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import paths
# from ripple.waveforms import IMRPhenomD_utils

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

# theta = np.array([25.0, 25.0, -0.8, -0.8])

# # Calculate the frequency regions
# coeffs = IMRPhenomD_utils.get_coeffs(theta)
# f1, f2, _, _, _, _ = IMRPhenomD_utils.get_transition_frequencies(
#     theta, coeffs[5], coeffs[6]
# )

# print(f2)
MSUN = 1.988409902147041637325262574352366540e30  # kg
G = 6.67430e-11  # m^3 / kg / s^2
C = 299792458.0  # m / s
gt = G * MSUN / (C ** 3.0)

f2 =  149.1018563859192 * (25. + 25.) * gt
plt.axvline(x=f2, color="k", alpha=0.4, ls="--")

plt.plot(freq, ori_error, label="Original")
plt.plot(freq, opt_error, label="Optimized")
plt.legend()
plt.xlabel(r"$Mf$")
plt.ylabel(r"$\Delta|\tilde{h}(f)|$")
plt.xlim(0.01, 0.09)
plt.ylim(0.0, 0.05)
plt.savefig(paths.figures / "loss_compare.pdf", bbox_inches="tight")
