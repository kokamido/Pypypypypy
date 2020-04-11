from Product.Glycolysis1D.Experiment import *
import numpy as np
from pylab import rcParams
from Product.Glycolysis1D.Glycolysis import run_higgins_0d


res = run_higgins_0d(3,1,np.arange(0,5000,0.01), np.array([1.1, 1.1]))[0][498000:]
print(res[-100])

rcParams['figure.figsize'] = 15,15
rcParams['legend.fontsize'] = 22
rcParams['axes.titlesize'] = 20
rcParams['xtick.labelsize'] = 22
rcParams['ytick.labelsize'] = 22
rcParams['grid.color'] = 'black'
rcParams['axes.grid'] = True


plt.plot(res[:,0], res[:,1],linewidth=6)
plt.grid(True)
ax = plt.gca()
ax.set_xticks(np.arange(0.5,3,0.5))
xlabels = np.arange(0.5,3,0.5).astype(str)
xlabels[-1]='$u$'
ax.set_xticklabels(xlabels)

ax.set_yticks(np.arange(0,6,1))
ylabels = np.arange(0,6,1).astype(str)
ylabels[-1]='$v$'
ax.set_yticklabels(ylabels)
plt.show()

plt.plot(np.arange(4980,5000,0.01), res[:,0],linewidth=6)
plt.grid(True)
ax = plt.gca()
ax.set_xticks(np.arange(4980.0,5000.1,2.5))
xlabels = np.arange(0.0,22.5,2.5).astype(str)
xlabels[-1]='$t$'
ax.set_xticklabels(xlabels)

ax.set_yticks(np.arange(0,2.5,0.5))
ylabels = np.arange(0,2.5,0.5).astype(str)
ylabels[-1]='$u$'
ax.set_yticklabels(ylabels)
plt.show()


plt.plot(np.arange(4980,5000,0.01), res[:,1],linewidth=6)
plt.grid(True)
ax = plt.gca()
ax.set_xticks(np.arange(4980.0,5000.1,2.5))
xlabels = np.arange(0.0,22.5,2.5).astype(str)
xlabels[-1]='$t$'
ax.set_xticklabels(xlabels)

ax.set_yticks(np.arange(0,6,1))
ylabels = np.arange(0,6,1).astype(str)
ylabels[-1]='$v$'
ax.set_yticklabels(ylabels)
plt.show()