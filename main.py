from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QIcon, QPixmap
from ui import Ui_MainWindow
import random

class Widget(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.setIcon(QIcon(QPixmap("ssha.jpg")))
        self.ui.pushButton_2.setIcon(QIcon(QPixmap("kvass.webp")))
        self.ui.pushButton_3.setIcon(QIcon(QPixmap("reich.webp")))

        self.ui.pushButton.clicked.connect(self.ssha)
        self.ui.pushButton_2.clicked.connect(self.taras)
        self.ui.pushButton_3.clicked.connect(self.reich)
        self.list1 = ["АМЕРИКА", "ТАРАС", "РЕЙХ"]

    def ssha(self):
        choices = random.choice(self.list1)
        self.ui.label_2.setText(choices)

        if self.ui.label_2.text() == "РЕЙХ":
            self.ui.label.setText("Ти виграв")
        if self.ui.label_2.text() == "ТАРАС":
            self.ui.label.setText("Ти програв")
        if self.ui.label_2.text() == "АМЕРИКА":
            self.ui.label.setText("нічия")

    def taras(self):
        choices = random.choice(self.list1)
        self.ui.label_2.setText(choices)

        if self.ui.label_2.text() == "АМЕРИКА":
            self.ui.label.setText("Ти виграв")
            
        if self.ui.label_2.text() == "РЕЙХ":
            self.ui.label.setText("Ти програв")
        if self.ui.label_2.text() == "ТАРАС":
            self.ui.label.setText("нічия")


    def reich(self):
        choices = random.choice(self.list1)
        self.ui.label_2.setText(choices)

        if self.ui.label_2.text() == "ТАРАС":
            self.ui.label.setText("Ти виграв")
        if self.ui.label_2.text() == "АМЕРИКА":
            self.ui.label.setText("Ти програв")
        if self.ui.label_2.text() == "РЕЙХ":
            self.ui.label.setText("нічия")




    


app = QApplication([])
ex = Widget()
ex.show()
app.exec_()