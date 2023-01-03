import numpy as np
import arviz as az
import matplotlib.pyplot as plt
import corner
%matplotlib inline

data_HMC = np.load('../data/chains_HMC.npz')
data_gaussian = np.load('../data/chains_gaussian.npz')

HMC_bestchain = data_HMC['chains'][np.argmax(data_HMC['log_prob'][:,-1])]
gaussian_bestchain = data_gaussian['chains'][np.argmax(data_gaussian['log_prob'][:,-1])]
import matplotlib as mpl
import corner
from matplotlib.ticker import MultipleLocator, FormatStrFormatter, AutoMinorLocator
from matplotlib.lines import Line2D
params = {
    "axes.labelsize": 32,
    "font.family": "serif",
    "font.size": 32,
    "axes.linewidth": 2,
    "legend.fontsize": 20,
    "xtick.labelsize": 20,
    "xtick.top": True,
    "xtick.direction": "in",
    "ytick.labelsize": 20,
    "ytick.right": True,
    "ytick.direction": "in",
    "axes.grid": False,
    "text.usetex": False,
    "savefig.dpi": 100,
    "lines.markersize": 14,
    "axes.formatter.limits": (-3, 3),
    "mathtext.fontset": "dejavuserif",
}


mpl.rcParams["text.latex.preamble"] = [r"\usepackage{amsmath}"]  # for \text command

mpl.rcParams.update(params)


def fill_corner(
    fig,
    data,
    ndim,
    axis,
    color="C0",
    true_val=None,
    zorder=1,
    lw=3,
    style="-",
    smooth1d=0.01,
    smooth2d=0.01,
    no_fill_contours=False,
    fill_contours=True,
    alpha=1,
    levels=[0.68, 0.95],
):
    for i in range(ndim):
        for j in range(i + 1):
            ax = fig.axes[np.sum(np.arange(i + 1)) + j]
            if i == j:
                ax.hist(
                    data[i],
                    bins=axis[i],
                    histtype="step",
                    lw=lw,
                    color=color,
                    density=True,
                    zorder=zorder,
                )
                ylim = ax.get_ylim()
                ax.set_xlim(axis[i][0], axis[i][-1])
                ax.set_ylim(ylim[0], ylim[1])
                if true_val is not None:
                    ax.vlines(
                        true_val[i], ylim[0], ylim[1], color=color, lw=lw, zorder=zorder
                    )
            elif j < i:
                corner.hist2d(
                    data[j],
                    data[i],
                    bins=[axis[j], axis[i]],
                    smooth=smooth2d,
                    plot_datapoints=False,
                    plot_density=False,
                    ax=ax,
                    levels=levels,
                    fill_contours=fill_contours,
                    smooth1d=smooth1d,
                    color=color,
                    no_fill_contours=True,
                    contour_kwargs={
                        "linewidths": lw,
                        "zorder": zorder,
                        "linestyles": style,
                        "colors": color,
                    },
                )
                ax.set_ylim(axis[i][0], axis[i][-1])
                ax.set_xlim(axis[j][0], axis[j][-1])
                if true_val is not None:
                    ax.scatter(
                        true_val[j],
                        true_val[i],
                        color=color,
                        marker="*",
                        s=100,
                        zorder=20,
                    )
                    ax.vlines(
                        true_val[j],
                        ax.get_ylim()[0],
                        ax.get_ylim()[1],
                        color=color,
                        lw=3,
                    )
                    ax.hlines(
                        true_val[i],
                        ax.get_xlim()[0],
                        ax.get_xlim()[1],
                        color=color,
                        lw=3,
                    )


Ndim = 7
fig = plt.figure(figsize=(20, 20))
grid = plt.GridSpec(Ndim, Ndim, wspace=0.1, hspace=0.1)

xlabel = [
    r"$m_{1}$",
    r"$m_{2}$",
    r"$s_1$",
    r"$s_2$",
    r"$D_L$",
    r"$t_c$",
    r"$\phi_c$",
]

lower_bound = [22.0, 0.23, -1.0, -1.0, 1300.0, -0.01, 0.0]
upper_bound = [28.0, 0.25, 1.0, 1.0, 1700.0, 0.01, 0.8]
axis = np.array([np.linspace(lower_bound[i], upper_bound[i], 20) for i in range(Ndim)])

for i in range(Ndim):
    for j in range(i + 1):
        ax = fig.add_subplot(grid[i, j])

fill_corner(
    fig,
    HMC_bestchain[::1000].T,
    Ndim,
    axis,
    style=["--", "-"],
    fill_contours=False,
    lw=2,
    levels=[0.68, 0.95],
    smooth2d=0.1,
)

fill_corner(
    fig,
    gaussian_bestchain[::1000].T,
    Ndim,
    axis,
    style=["--", "-"],
    fill_contours=False,
    lw=2,
    levels=[0.68, 0.95],
    smooth2d=0.1,
    color="C1",
)