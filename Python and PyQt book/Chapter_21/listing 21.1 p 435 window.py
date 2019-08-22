# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()             # Создаем окно
window.setWindowTitle("Заголовок окна")  # Указываем заголовок
window.resize(300, 50)                   # Минимальные размеры
window.show()                            # Отображаем окно
i=5
print("123")
sys.exit(app.exec_())
print("456")
i=5

window.setVisible(True)
print("789")
