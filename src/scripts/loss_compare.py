import numpy as np
import matplotlib.pyplot as plt
import paths

(freq, ori_error, opt_error) = np.loadtxt(paths.data / "loss_compare.txt", unpack=True)

plt.plot(freq, ori_error, label='original')
plt.plot(freq, opt_error, label='optimized')
plt.legend()
plt.xlabel(r'$Mf$')
plt.ylabel(r'$\Delta|\tilde{h}(f)|$')
plt.savefig(paths.figures / "loss_compare.pdf", bbox_inches="tight")