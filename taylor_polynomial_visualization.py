
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import math

X = np.linspace(-5, 5, 1000, endpoint=True)
#C, S = np.cos(X), np.sin(X)
n = 1

def taylor_polynomial_for_exp(x):
    global n
    s = 0
    if n >= 0:
        step = 1
    else:
        step = -1
    for i in range(0,n+1,step):
        s += x**i/math.factorial(i)
    return s

v_taylor_polynomial_for_exp = np.vectorize(taylor_polynomial_for_exp)



def plot_func(func, ax=None):
    Y = func(X)
    if ax == None:
        return plt.plot(X, Y)
    else:
        return ax.plot(X, Y)

for i in range(1):

    n += 1

def name_for_taylor_ex(n):
    name = ''
    for i in range(n+1):
        if i == 0:
            name += '1'
        elif i == 1:
            name += '+x'
        else:
            name += '+x^'+str(i)+'/'+str(i)+'!'
    return name

class Index(object):
    ind = 2
    fig = None
    ax = plt.gca()
    first = True

    def draw(self):
        global n
        n = self.ind
        self.ax.clear()
        line1, = plot_func(np.exp, self.ax)
        line2, = plot_func(v_taylor_polynomial_for_exp, self.ax)
        self.ax.legend((line1, line2), ('e^x', name_for_taylor_ex(n)))
        self.ax.set_title('taylor polynomial when n = '+str( n))
        self.ax.set_ylim([-20,160])

        plt.draw()

    def next(self, event):
        self.ind += 1
        self.draw()

    def prev(self, event):
        self.ind -= 1
        self.draw()

callback = Index()
callback.draw()

axprev = plt.axes([0.7, 0.00, 0.1, 0.075])
axnext = plt.axes([0.81, 0.00, 0.1, 0.075])
bnext = Button(axnext, 'Next')
bnext.on_clicked(callback.next)
bprev = Button(axprev, 'Previous')
bprev.on_clicked(callback.prev)

plt.show()
