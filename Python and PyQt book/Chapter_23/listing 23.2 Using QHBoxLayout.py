# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets, QtCore
import sys, time
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()              # Родительский компонент — окно
window.setWindowTitle("QHBoxLayout")
window.resize(300, 60)
button1 = QtWidgets.QPushButton("1")
button2 = QtWidgets.QPushButton("2")
button3 = QtWidgets.QPushButton("3")
button4 = QtWidgets.QPushButton("4")
button5 = QtWidgets.QPushButton("5")
hbox = QtWidgets.QHBoxLayout()            # Создаем контейнер

"""hbox.addWidget(button1, 3, QtCore.Qt.AlignRight)
hbox.addWidget(button2, stretch=10)
hbox.addWidget(button3, 10, alignment=QtCore.Qt.AlignRight)
"""
hbox.addWidget(button1)
hbox.insertWidget(-1, button2) # Добавление в конец
hbox.insertWidget(0, button3)  # Добавление в начало
hbox.setContentsMargins(2, 4, 2, 4)
m = QtCore.QMargins(4, 2, 4, 2)
hbox.setContentsMargins(m)



"""hbox.addWidget(button1)                   # Добавляем компоненты
hbox.addWidget(button2)"""
window.setLayout(hbox)                    # Передаем ссылку родителю"""
window.show()
#time.sleep(5);
hbox.replaceWidget(button1, button5, options = QtCore.Qt.FindDirectChildrenOnly)
sys.exit(app.exec_())
print("12345")
