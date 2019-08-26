# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets, QtCore
import sys, time

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()             # Создаем окно
window.setWindowTitle("Заголовок окна")  # Указываем заголовок
window.resize(300, 50)                   # Минимальные размеры
#
"""window.setWindowFlags(QtCore.Qt.Window |
                      QtCore.Qt.FramelessWindowHint |
                      QtCore.Qt.WindowTitleHint |
                      QtCore.Qt.WindowStaysOnTopHint)"""
window.setWindowOpacity(0.5)
print(window.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
print("456")
window.show()                            # Отображаем окно
"""print(window.isVisible())
print(window.isHidden())
i=5
print("123")
time.sleep(1)
window.hide()
print(window.isVisible())
print(window.isHidden())
time.sleep(1)
window.setVisible(True)
print(window.isVisible())
print(window.isHidden())
window.setWindowTitle("qwerty123")
time.sleep(3)"""
sys.exit(app.exec_())
print("456")
i=5

window.setVisible(True)
print("789")
