# coding: utf-8
from PyQt5 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Первая программа на PyQt")
window.resize(300, 70)
label = QtWidgets.QLabel("<center>Привет, Мир!</center>")
btnQuit = QtWidgets.QPushButton("&3акрыть окно")
vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(label)
vbox.addWidget(btnQuit)
window.setLayout(vbox)
btnQuit.clicked.connect(app.quit)
window.show()

sys.exit(app.exec_(print("qwerty")))
