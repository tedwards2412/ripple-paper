import matplotlib.pyplot as plt
import numpy as np
import paths
import matplotlib as mpl
import corner

params = {
    "font.size": 18,
    "legend.fontsize": 18,
    "legend.frameon": False,
    "axes.labelsize": 18,
    "axes.titlesize": 18,
    # "axes.labelpad": 30,
    "axes.unicode_minus": False,
    "xtick.labelsize": 10,
    "ytick.labelsize": 10,
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

# file = np.load(paths.data / "ripple_flowMC_results.npz")
data_HMC = np.load(paths.data / "chains_HMC.npz")
HMC_bestchain = data_HMC["chains"][np.argmax(data_HMC["log_prob"][:, -1])]


def ms_to_Mc_eta(m):
    r"""
    Converts binary component masses to chirp mass and symmetric mass ratio.
    Args:
        m: the binary component masses ``(m1, m2)``
    Returns:
        :math:`(\mathcal{M}, \eta)`, with the chirp mass in the same units as
        the component masses
    """
    m1, m2 = m
    return (m1 * m2) ** (3 / 5) / (m1 + m2) ** (1 / 5), m1 * m2 / (m1 + m2) ** 2


labels = ["$M_c$", "$\eta$", "$\chi_1$", "$\chi_2$", "D", "$t_c$", "$\phi_c$"]
n_dim = 7
# Mc, eta, chi1, chi2, dist, tc, phic, inclination, polarization_angle, ra, dec,
m1 = 30
m2 = 25
Mc, eta = ms_to_Mc_eta(np.array([m1, m2]))
distance = 1600

true_params = np.array(
    [Mc, eta, 0.3, -0.4, distance, 0.0, 0.0, np.pi / 3, np.pi / 3, np.pi / 3, np.pi / 3]
)

# Plot all chains
figure = corner.corner(HMC_bestchain, labels=labels, labelpad=0.1)

# Extract the axes
axes = np.array(figure.axes).reshape((n_dim, n_dim))

# Loop over the diagonal
for i in range(n_dim):
    ax = axes[i, i]
    ax.axvline(true_params[i], color="C1", alpha=0.5)

# Loop over the histograms
for yi in range(n_dim):
    for xi in range(yi):
        ax = axes[yi, xi]
        ax.axvline(true_params[xi], color="C1", alpha=0.5)
        ax.axhline(true_params[yi], color="C1", alpha=0.5)
        ax.plot(true_params[xi], true_params[yi], "s", color="C1", alpha=0.5)

figure.set_size_inches(10, 10)
plt.savefig(paths.figures / "PE.pdf", bbox_inches="tight")

