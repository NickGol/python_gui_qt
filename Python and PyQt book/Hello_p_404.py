# coding: utf-8
from PyQt5 import QtCore, QtWidgets
class MyWindow(QtWidgets.QWidget):
    def ___init__(self, parent=None):
        QtWidgets.QWidget.___init__(self, parent)
        self.label = QtWidgets.QLabel("Привет, мир!")
        self.label.setAlignment(QtCore.Qt.AlignHCenter)
        self.btnQuit = QtWidgets.QPushButton("&3акрыть окно")
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addwidget(self.label)
        self.vbox.addwidget(self.btnQuit)
        self.setLayout(self.vbox)
        self.btnQuit.clicked.connect(QtWidgets.qApp.quit)
if __name__	== "__main__" :
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()	# Создаем экземпляр класса
    window.setWindowTitle("ООП-стиль создания окна")
    window.resize(300, 70)
    window.show()	# Отображаем окно
    sys.exit(app.exec_()) # Запускаем цикл обработки событий