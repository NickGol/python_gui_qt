# ------------------------------------------------------
# ---------------------- main.py -----------------------
# ------------------------------------------------------
from PyQt5.QtWidgets import*
from PyQt5.uic import loadUi

from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)

import numpy as np
import random


from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg
from pyqtgraph.ptime import time



     
class MatplotlibWidget(QMainWindow):
    
    def __init__(self):
        
        QMainWindow.__init__(self)

        loadUi("qt_designer.ui",self)

        self.setWindowTitle("PyQt5 & Matplotlib Example GUI")

        # self.pushButton_generate_random_signal.clicked.connect(self.update_graph)
        self.pushButton_generate_random_signal.clicked.connect(self.update)

        # self.addToolBar(NavigationToolbar(self.MplWidget.canvas, self))

        # self.MplWidget.canvas.axes = self.MplWidget.canvas.figure.add_subplot(111)
        self.MplWidget.setLabel('bottom', 'Index', units='B')
        self.MplWidget.setBackground([227, 255, 15, 10])
        # pg.setConfigOption('background', 'w')
        # self.MplWidget.setBackground('none')

        self.nPlots = 100
        self.nSamples = 500
        # curves = [self.MplWidget.plot(pen=(i,nPlots*1.3)) for i in range(nPlots)]
        self.curves = []
        for i in range(self.nPlots):
            self.c = pg.PlotCurveItem(pen=(i, self.nPlots * 1.3))
            self.MplWidget.addItem(self.c)
            self.c.setPos(0, i * 6)
            self.curves.append(self.c)

        self.MplWidget.setYRange(0, self.nPlots * 6)
        self.MplWidget.setXRange(0, self.nSamples)
        self.MplWidget.resize(600, 900)

        rgn = pg.LinearRegionItem([self.nSamples / 5., self.nSamples / 3.])
        self.MplWidget.addItem(rgn)

        self.data = np.random.normal(size=(self.nPlots * 23, self.nSamples))
        self.ptr = 0
        self.lastTime = time()
        self.fps = None
        self.count = 0
        self.cnt = 0

    def update(self):
        # global curve, data, ptr, p, lastTime, fps, nPlots, count
        self.cnt += 1
        if self.cnt > 255:
            self.cnt = 0
        self.MplWidget.setBackground([255, 157, 0, self.cnt])
        self.count += 1
        # print "---------", count
        for i in range(self.nPlots):
            self.curves[i].setData(self.data[(self.ptr + i) % self.data.shape[0]])

        # print "   setData done."
        self.ptr += self.nPlots
        self.now = time()
        self.dt = self.now - self.lastTime
        self.lastTime = self.now
        if self.fps is None:
            self.fps = 1.0 / self.dt
        else:
            s = np.clip(self.dt * 3., 0, 1)
            self.fps = self.fps * (1 - s) + (1.0 / self.dt) * s
        self.MplWidget.setTitle('%0.2f fps' % self.fps)
        # app.processEvents()  ## force complete redraw for every plot




    # def update_graph(self):
    #
    #     fs = 500
    #     f = random.randint(1, 100)
    #     ts = 1/fs
    #     length_of_signal = 1000
    #     t = np.linspace(0,1,length_of_signal)
    #
    #     cosinus_signal = np.cos(2*np.pi*f*t)
    #     sinus_signal = np.sin(2*np.pi*f*t)
    #
    #     self.MplWidget.canvas.axes.clear()
    #     # self.MplWidget.canvas.axes.plot(t, cosinus_signal)
    #     self.MplWidget.canvas.axes.plot(t, sinus_signal)
    #     self.MplWidget.canvas.axes.legend(('cosinus', 'sinus'),loc='upper right')
    #     self.MplWidget.canvas.axes.set_title('Cosinus - Sinus Signal')
    #     self.MplWidget.canvas.draw()
        

app = QApplication([])
window = MatplotlibWidget()
timer = QtCore.QTimer()
timer.timeout.connect(window.update)
timer.start(0)
window.show()

app.exec_()




















