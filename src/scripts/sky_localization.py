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
}

# mpl.rcParams["text.latex.preamble"] = [r"\usepackage{amsmath}"]  # for \text command

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
) = np.loadtxt(paths.data / "sky_localization.txt", unpack=True)

plt.figure(figsize=(7, 5))
bins = np.geomspace(0.1, np.max(sky_error_list), 50)
# bins = np.linspace(0.0, np.max(sky_error_list), 80)
plt.hist(sky_error_list, bins=bins, density=True, alpha=0.3, color="C0")
plt.hist(sky_error_list, bins=bins, density=True, histtype="step", color="C0")

plt.xscale("log")
plt.xlim(0.1, 300)
plt.xlabel("Sky Localization Error [deg$^2$]")
plt.ylabel("Probability")
plt.savefig(paths.figures / "sky_localization.pdf", bbox_inches="tight")

