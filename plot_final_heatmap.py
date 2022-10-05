import matplotlib.pylab as plt
import matplotlib as mpl
import numpy as np
import pandas as pd

heatmap = pd.DataFrame(np.genfromtxt('combined_data.csv', delimiter=' '))

heatmapT = heatmap.T

cmap='jet_r'

fig, ax = plt.subplots(1,1)
heatmap = ax.pcolormesh(heatmapT, cmap=cmap, vmin = 4, vmax=25) #[2,5,10,15,20,40]
contours = ax.contour(heatmapT, [5, 10,15, 20])
fig.colorbar(heatmap, extend='both',ticks=[5,10,15, 20], label = 'Critical casualty area ($m^2$)')
#fig.colorbar(contours,ticks=[5,10,20])

ax.set_xlabel('Years from 2020')
ax.set_ylabel('Inclination ($^\circ$)')
plt.xticks(range(0,151,10))
plt.yticks(range(0,181,20))

ax.set_xticklabels(range(-70,81,10))
ax.set_yticklabels(range(0,91,10))
ax.set_ylim(0,180)
ax.set_xlim(0,150)
plt.show()

