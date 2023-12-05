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

c1 = "#102F68"  # blue
c2 = "#B02423"  # red

# f2 =  149.1018563859192 * (25. + 25.) * gt
# plt.axvline(x=f2, color="k", alpha=0.4, ls="--")

f_ins = 0.018
f_rd = 149.1018563859192 * (25.0 + 25.0) * gt

data = np.loadtxt(paths.data / "0154_compare.dat")

f_uniform = data[:, 0]
NR_amp = data[:, 1]
NR_angle = data[:, 2]
IMR_amp = data[:, 3]
IMR_angle = data[:, 4]
IMR_opt_amp = data[:, 5]
IMR_opt_angle = data[:, 6]

plt.semilogx(
    f_uniform,
    (NR_amp - IMR_amp)/ NR_amp,
    label="IMR original",
    linestyle=(0, (3, 1)),
    color=c1,
    lw=2,
)
plt.semilogx(
    f_uniform, (NR_amp - IMR_opt_amp)/ NR_amp, label="IMR optimized", color=c2, lw=2
)
plt.axvline(x=f_ins, color="k", alpha=0.5, linestyle=(0, (1, 1.05)))
plt.axvline(x=f_rd, color="k", alpha=0.5, linestyle=(0, (1, 1.05)))

# plt.plot(freq, ori_error, label="Original")
# plt.plot(freq, opt_error, label="Optimized")
plt.legend()
plt.xlabel(r"$Mf$")
# plt.ylabel(r"$\Delta|\tilde{h}(f)|$")
plt.ylabel(r"$(\tilde{h}-\tilde{h}_{\mathrm{NR}})/\tilde{h}_{\mathrm{NR}}$")
# plt.xlim(0.01, 0.2)
# plt.ylim(0.0, 0.05)
plt.xscale("log")
plt.savefig(paths.figures / "loss_compare.pdf", bbox_inches="tight")
