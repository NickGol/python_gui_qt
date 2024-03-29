import pyqtgraph.examples
pyqtgraph.examples.run()

from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg
from pyqtgraph.ptime import time

app = QtGui.QApplication([])

p = pg.plot()
p.setWindowTitle('pyqtgraph example: PlotSpeedTest')
p.setRange(QtCore.QRectF(0, -3, 50000, 6))
p.setLabel('bottom', 'Index', units='B')
curve = p.plot()

# curve.setFillBrush((0, 0, 100, 100))
# curve.setFillLevel(0)

# lr = pg.LinearRegionItem([100, 4900])
# p.addItem(lr)

data = np.random.normal(size=(50, 50000))
for i in range(50):
    data[i] = 3*np.sin(i*0.1+np.arange(50000)/100)
ptr = 0
lastTime = time()
fps = None


def update():
    global curve, data, ptr, p, lastTime, fps
    curve.setData(data[ptr % 10])
    ptr += 1
    now = time()
    dt = now - lastTime
    lastTime = now
    if fps is None:
        fps = 1.0 / dt
    else:
        s = np.clip(dt * 3., 0, 1)
        fps = fps * (1 - s) + (1.0 / dt) * s
    p.setTitle('%0.5f dt' % dt)
    app.processEvents()  ## force complete redraw for every plot


timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(0)

## Start Qt event loop unless running in interactive mode.
if __name__ == '__main__':
    import sys

    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
