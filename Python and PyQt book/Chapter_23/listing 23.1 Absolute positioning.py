# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Абсолютное позиционирование")
window.resize(300, 120)
label = QtWidgets.QLabel("Текст надписи", window)
button = QtWidgets.QPushButton("Текст на кнопке", window)
"label.setGeometry(10, 10, 280, 60)"
label.resize(100, 100)
button.resize(280, 30)
"button.move(10, 80)"
window.show()
sys.exit(app.exec_())
