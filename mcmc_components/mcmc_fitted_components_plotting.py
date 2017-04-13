import numpy as np
import matplotlib
matplotlib.rcParams.update({'font.size': 20})
import matplotlib.pyplot as plt
# import seaborn
# seaborn.set_style("whitegrid", {'axes.grid' : False})

data = np.genfromtxt('mcmc_fitted_components_90ns.dat',
	names=True
	)
time = data['time']*1e9 # ns
signal = data['signal']*1e3 # raw data, mV
one_signal = data['one_signal']*1e3
two_signal = data['two_signal']*1e3

plt.figure()
plt.plot(time,signal,label='data',color='grey')
plt.plot(time,one_signal+two_signal,label='Bayesian fit', color='black')
plt.plot(time,one_signal,label='Bayesian fit 1st photon', color='blue')
plt.plot(time,two_signal,label='Bayesian fit 2nd photon',color='red')
plt.xlim(0,1500)
plt.xlabel('time (ns)')
plt.ylabel('voltage (mV)')
# plt.legend()
plt.savefig('mcmc_fitted_components_90ns.svg')
plt.show()