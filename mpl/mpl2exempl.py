import matplotlib.pyplot as plt
import numpy as np
from numpy.matlib import randn

fig = plt.figure()
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)

plt.plot(randn(100).cumsum(), 'k--')
f = ax1.hist(randn(100), bins=20, color='y', alpha=0.9)
ax2 = sc