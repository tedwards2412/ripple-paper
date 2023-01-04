import numpy as np
import matplotlib.pyplot as plt
import paths

(catalog_num, ori_loss, opt_loss) = np.loadtxt(paths.data / "mismatch_hist.txt", unpack=True)
bins = np.arange(-5, -1, 0.125)

plt.hist(np.log10(ori_loss), bins=bins, alpha=0.5, label='original')
plt.hist(np.log10(opt_loss), bins=bins, alpha=0.5, label='optimized')
plt.legend()
plt.xlabel('$\log(\mathcal{M})$')
plt.ylabel('Count')
plt.savefig(paths.figures / "mismatch_hist.pdf", bbox_inches="tight")