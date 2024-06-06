import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import paths
from scipy import stats

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

# palette = ['#2e4854', '#557b82','#bab2a9', '#c98769','#a1553a']
palette = ['#306B37', 'darkgoldenrod', '#3F7BB6', '#BF4145', "#cf630a"]

plt.rcParams['axes.prop_cycle'] = plt.cycler(color=palette)

M_list = np.linspace(10, 100, 10)
loop_time_list_lalsuite = np.loadtxt(paths.data / "loop_time_lalsuite.txt")
loop_time_list = np.loadtxt(paths.data / "loop_time.txt")
vmapped_time_list = np.loadtxt(paths.data / "vmapped_time.txt")
gpu_time_list = np.loadtxt(paths.data / "vmapped_time_gpu.txt")
gpu_time_list_float32 = np.loadtxt(paths.data / "vmapped_time_gpu_float32.txt")

plt.plot(M_list, loop_time_list_lalsuite * 1000, label="Lalsuite", lw = 3, color="k")
plt.plot(M_list, loop_time_list * 1000, label="CPU (loop)", lw = 2, ls="-.")
plt.plot(M_list, vmapped_time_list * 1000, label="CPU (vmap)", ls="--", lw = 2)
plt.plot(M_list, gpu_time_list * 1000, label="GPU", ls=":", lw = 2 )
plt.plot(M_list, gpu_time_list_float32 * 1000, label="GPU float32", ls=":", lw = 2 )
plt.yscale("log")
plt.xlabel("Total mass, $M$ [M$_\odot$]")
plt.ylabel("Time [ms]")
plt.ylim(1e-3, 8e1)
plt.legend(loc="upper right")

plt.savefig(paths.figures / "timing.pdf", bbox_inches="tight")