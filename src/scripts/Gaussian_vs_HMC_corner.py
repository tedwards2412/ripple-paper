import numpy as np
import arviz as az
import matplotlib.pyplot as plt
import corner
%matplotlib inline

data_HMC = np.load('../data/chains_HMC.npz')
data_gaussian = np.load('../data/chains_gaussian.npz')

HMC_bestchain = data_HMC['chains'][np.argmax(data_HMC['log_prob'][:,-1])]
gaussian_bestchain = data_gaussian['chains'][np.argmax(data_gaussian['log_prob'][:,-1])]

acl_HMC = az.autocorr(HMC_bestchain.T).T
acl_gaussian = az.autocorr(gaussian_bestchain.T).T
print(acl_HMC.shape, acl_gaussian.shape)
plt.figure(figsize=(10,9))
plt.plot(acl_HMC[::100,0], label='HMC')
plt.plot(acl_gaussian[::100,0], label='Gaussian')
plt.xlim(0,1000)
plt.xlabel('Lag')
plt.ylabel('Autocorrelation')
for i in range(7):
    print(az.ess(HMC_bestchain[::100,i]), az.ess(gaussian_bestchain[::100,i]))