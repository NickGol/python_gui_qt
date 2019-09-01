# -*- coding: utf-8 -*-
"""from PyQt5 import QtCore, QtGui, QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Изменение цвета фона окна")
window.resize(300, 100)
pal = window.palette()
pal.setColor(QtGui.QPalette.Normal, QtGui.QPalette.Window,
             QtGui.QColor("#008800"))
pal.setColor(QtGui.QPalette.Inactive, QtGui.QPalette.Window,
             QtGui.QColor("#ff0000"))
window.setPalette(pal)
label = QtWidgets.QLabel("Текст надписи")
label.setAlignment(QtCore.Qt.AlignHCenter)
label.setStyleSheet("background-color: #ffffff;")
label.setAutoFillBackground(True)
frame = QtWidgets.QPushButton("qwerty")
frame.setGeometry(0,0,50,50)
frame.setStyleSheet("background-color: #ff00ff;")
frame.setAutoFillBackground(True)
frame1 = QtWidgets.QPushButton("qwerty")
frame1.setGeometry(0,0,50,50)
frame1.setStyleSheet("background-color: #ff0000;")
frame1.setAutoFillBackground(True)
vbox = QtWidgets.QVBoxLayout()
vbox1 = QtWidgets.QVBoxLayout()
vbox.addWidget(label)
vbox.addWidget(frame)
vbox.addWidget(frame1)
vbox.addWidget(frame)
window.setLayout(vbox)
window.show()
sys.exit(app.exec_())
"""

import sys
from PyQt5.QtWidgets import (QWidget, QGridLayout,
                             QPushButton, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        grid = QGridLayout()
        self.setLayout(grid)

        names = ['Cls', 'Bck', '', 'Close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']

        positions = [(i, j) for i in range(5) for j in range(4)]

        for position, name in zip(positions, names):

            if name == '':
                continue
            button = QPushButton(name)
            grid.addWidget(button, *position)

        self.move(300, 150)
        self.setWindowTitle('Calculator')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())