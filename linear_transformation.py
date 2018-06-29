import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
import math

init_matrix = np.array([
    [1,0],
    [0,1]])
#init_matrix = np.array([
#    [0.2,1],
#    [-0.4,-2]])
mode='normal'
grid_on = True
np.set_printoptions(precision=3)

def get_base_shape(step=0.1):
    """
    return X such that plt.plot(X[:,0],X[:,1]) creates a base shape.
    """
    corners_x = [0,0,3,3,0]
    corners_y = [0,2,2,0,0]

    X = []
    for i in range(len(corners_x)-1):
        t = 0
        x1 = corners_x[i]
        x2 = corners_x[i+1]
        y1 = corners_y[i]
        y2 = corners_y[i+1]
        while True:
            _x = x1+t*(x2-x1)
            _y = y1+t*(y2-y1)
            #x.append(_x)
            #y.append(_y)
            X.append((_x, _y))
            if t == 1:
                break
            t += step
            if t > 1:
                t = 1


    return np.array(X)

fig, ax = plt.subplots(figsize=(10,8))
plt.subplots_adjust(left=0.25, bottom=0.25)
#x = np.arange(-2, 2, 0.1)
#y = np.sin(x)
X = get_base_shape()
gridlines = [None,None]
grid_range = [-5,5]
grid_count = grid_range[1] - grid_range[0]
if not grid_on:
    grid_count = 0
gridlines[0] = [np.array([[-100,i],[100,i]]) for i in range(grid_range[0],grid_range[1])]
gridlines[1] = [np.array([[i,-100],[i,100]]) for i in range(grid_range[0],grid_range[1])]
grid = []
plt.plot(X[:,0], X[:,1], lw=2, color='green', alpha=0.5)
l, = plt.plot(X[:,0], X[:,1], lw=2, color='red')
for i in range(2):
    for j in range(grid_count):
        line = gridlines[i][j]
        p = [None,None]
        p[0] = line.copy()
        p[1], = plt.plot(line[:,0], line[:,1], color='brown',alpha=0.3)
        grid.append(p)
hlines = [i for i in range(-4, 5)]
vlines = [i for i in range(-4, 5)]
for line in hlines:
    plt.axhline(y=line, alpha=0.3, color='k')
for line in vlines:
    plt.axvline(x=line, alpha=0.3, color='k')
plt.axis([-5, 5, -5, 5])

axcolor = 'lightgoldenrodyellow'
sa = [[None,None],[None,None]]
s = [[None,None],[None,None]]
for i in range(4):
    ii = i//2
    jj = i%2
    sa[ii][jj] = plt.axes([0.25,0.14-i*0.03, 0.65, 0.02], facecolor=axcolor)
    s[ii][jj] = Slider(sa[ii][jj], 'a{}{}'.format(ii,jj), -3.0, 3.0, valinit=init_matrix[ii,jj])
sa_t = plt.axes([0.25, 0.17, 0.65, 0.02], facecolor=axcolor)

s_t = Slider(sa_t, 't', 0, 1.0, valinit=1)


def update(val):
    #l.set_ydata(amp*np.sin(2*np.pi*freq*t))
    #l.set_ydata(np.sin(x)*(samp.val+sfreq.val))
    A = np.array([[s[0][0].val,s[0][1].val],[s[1][0].val,s[1][1].val]])
    if mode == 'normal':
        O = np.identity(2)
        A_hat = O + (A-O)*s_t.val
    elif mode == 'rotation':
        theta = s_t.val*2*math.pi
        r = np.array([[math.cos(theta), -math.sin(theta)],
                      [math.sin(theta), math.cos(theta)]])
        A_hat = r.dot(A)
    new_X = (A_hat.dot(X.T).T)
    for i in range(len(grid)):
        points, line = grid[i]
        new_points = A_hat.dot(points.T).T
        line.set_xdata(new_points[:,0])
        line.set_ydata(new_points[:,1])
    l.set_xdata(new_X[:,0])
    l.set_ydata(new_X[:,1])
    fig.canvas.draw_idle()
    print('\nT = \n',np.round_(A_hat,decimals=3))
    print('determinant: ', np.linalg.det(A_hat))
s[0][0].on_changed(update)
s[1][0].on_changed(update)
s[0][1].on_changed(update)
s[1][1].on_changed(update)
s_t.on_changed(update)

resetax = plt.axes([0.8, 0.015, 0.05, 0.02])
button = Button(resetax, 'Round', color=axcolor, hovercolor='0.975')
resetaxf = plt.axes([0.7, 0.015, 0.05, 0.02])
buttonf = Button(resetaxf, 'Roundf', color=axcolor, hovercolor='0.975')


def Round(event):
    #s[0][0].reset()
    #s[1][0].reset()
    #s[0][1].reset()
    #s[1][1].reset()
    for i in range(4):
        s_ = s[i//2][i%2]
        s_.set_val( round(s_.val))
    #s_t.reset()

button.on_clicked(Round)
def Roundf(event):
    for i in range(4):
        s_ = s[i//2][i%2]
        s_.set_val( round(s_.val, 2))
    s_t.set_val(round(s_t.val, 2))
buttonf.on_clicked(Roundf)

rax = plt.axes([0.025, 0.5, 0.15, 0.15], facecolor=axcolor)
radio = RadioButtons(rax, ('normal', 'rotation'), active=0)


def colorfunc(label):
    global mode
    mode=label
    s_t.set_val(0)
    #l.set_color(label)
    #fig.canvas.draw_idle()
radio.on_clicked(colorfunc)

plt.show()
