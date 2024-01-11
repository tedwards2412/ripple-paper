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

(
    Mc,
    eta,
    chi1,
    chi2,
    dist,
    tc,
    phic,
    inclination,
    polarization_angle,
    ra,
    dec,
    sky_error_list,
    SNR_list,
    Mchirp_err_list,
) = np.loadtxt(paths.data / "sky_localization.txt", unpack=True)


# Load GWbench data
GWbench_Mcs = np.loadtxt(paths.data / "GWbench_Mcs.txt")

plt.figure(figsize=(7, 5))
bins = np.geomspace(0.1, np.max(Mchirp_err_list), 30)
plt.hist(Mchirp_err_list, bins=bins, density=True, alpha=0.3, color="C0")
plt.hist(Mchirp_err_list, bins=bins, density=True, histtype="step", color="C0", lw=2, label="Ripple")

plt.hist(GWbench_Mcs, bins=bins, density=True, alpha=0.3, color="C3")
plt.hist(GWbench_Mcs, bins=bins, density=True, histtype="step", color="C3", lw=2, label="GWBench")

rel_errors = (Mchirp_err_list - GWbench_Mcs) / GWbench_Mcs

print(rel_errors.min(), rel_errors.max(), rel_errors.mean(), rel_errors.std())

plt.xscale("log")
plt.xlim(0.08, 10.0)
plt.xlabel("Chrip Mass Error [$\mathrm{M}_\odot$]")
plt.ylabel("Probability")
plt.legend()
plt.savefig(paths.figures / "chirp_mass_error.pdf", bbox_inches="tight")

