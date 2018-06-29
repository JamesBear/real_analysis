
import numpy as np
import matplotlib.pyplot as plt
import math
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.widgets import Slider, Button, RadioButtons

mpl.rcParams['legend.fontsize'] = 10

plt.style.use('dark_background')
#fig = plt.figure()
##ax = fig.gca(projection='3d')
#gs = gridspec.GridSpec(1, 2, width_ratios=[3, 1])
fig,(ax2,ax) = plt.subplots(1,2, figsize=(10,7))
#fig,ax = plt.subplots(figsize=(15,7))
plt.subplots_adjust(left=0.1, bottom=0.25)

c = (215/255,215/255,53/255)

# Prepare arrays x, y, z
theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
x = np.linspace(0, 4, 1000)
y = 0.5*np.cos(math.pi*10*x)+0.5
ax2.plot(x, y, color=c)
ax2.axis('equal')
ax2.axis([0,4,0,1])
ax2.set_autoscale_on(False)
cycles_per_second = 2
t = np.linspace(0, 2*math.pi*cycles_per_second*4, 1000)
r = 0.5*np.cos(math.pi*10*t*(1/cycles_per_second/2/math.pi))+0.5
xr = r*np.cos(t)
yr = r*np.sin(t)
l, = ax.plot(xr, yr, color=c)
ax.axis('equal')
ax.set_xlim([-1,1])
ax.set_ylim([-1,1])
ax.set_title('{:.2f} cycles/second'.format(cycles_per_second))

axcolor = 'lightgoldenrodyellow'
axfreq = plt.axes([0.08, 0.1, 0.85, 0.03], facecolor=axcolor)
f0 = 2
sfreq = Slider(axfreq, 'Cycles/s', 0.05, 7.0, valinit=f0)

def update(val):
    cycles_per_second = val
    ax.set_title('{:.2f} cycles/second'.format(cycles_per_second))
    t = np.linspace(0, 2*math.pi*cycles_per_second*4, 1000)
    r = 0.5*np.cos(math.pi*10*t*(1/cycles_per_second/2/math.pi))+0.5
    xr = r*np.cos(t)
    yr = r*np.sin(t)
    #l.set_ydata(amp*np.sin(2*np.pi*freq*t))
    l.set_xdata(xr)
    l.set_ydata(yr)
    fig.canvas.draw_idle()
sfreq.on_changed(update)



plt.show()
