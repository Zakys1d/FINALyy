#конвертація ui файлу в python файл (писати в терміналі)
python -m PyQt5.uic.pyuic -x untitled.ui -o ui.py



#шаблон python файлу
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QIcon, QPixmap
from ui import Ui_MainWindow

class Widget(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

app = QApplication([])
ex = Widget()
ex.show()
app.exec_()


#створення функцій
def назва_функції(self):
  pass


#виклик функції до кнопки
self.ui.назва_кнопки.clicked.connect(self.назва_функції)



#встановлення зображення на кнопку
self.ui.назва_кнопки.setIcon(QIcon(QPixmap("назва_зображення.jpg")))

#встановлення тексту на кнопку
self.ui.назва_кнопки.setText("текст")

#перевірка тексту на кнопці
if self.ui.назва_кнопки.text() == "текст":
  pass


#створення списку
list1 = ["текст1","текст2","текст3"]

#вибір випадкового елементу зі списку
import random #потрібно відключати зверху
n = random.choice(назва_списку)
