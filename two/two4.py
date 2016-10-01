import pylab
import numpy as np


t = np.arange(-50, 50.01, 0.01)


pylab.ion()
for a in range(50):
    xlist = np.sin(t + a)
    ylist = np.cos(2*t)
    pylab.clf()
    pylab.plot(xlist, ylist)
    pylab.draw()
    pylab.pause(0.3)

pylab.close()