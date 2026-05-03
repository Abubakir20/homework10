import json
from PyQt5.QtWidgets import *


from fruits import FruitsWindow
from vegetables import VegetablesWindow
from drinks import DrinksWindow
from accessories import AccessoriesWindow
from cart import CartWindow


# load data (school style)
f = open("data.json", "r")
products = json.load(f)
f.close()


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Shop")

        self.cart = []

        self.v_lay = QVBoxLayout()

        self.btn_fruits = QPushButton("Fruits")
        self.btn_veg = QPushButton("Vegetables")
        self.btn_drinks = QPushButton("Drinks")
        self.btn_acc = QPushButton("Accessories")
        self.btn_cart = QPushButton("Cart")
        self.btn_exit = QPushButton("Exit")

        self.btn_fruits.clicked.connect(self.fruits)
        self.btn_veg.clicked.connect(self.veg)
        self.btn_drinks.clicked.connect(self.drinks)
        self.btn_acc.clicked.connect(self.acc)
        self.btn_cart.clicked.connect(self.cart_open)
        self.btn_exit.clicked.connect(self.close)

        self.v_lay.addWidget(self.btn_fruits)
        self.v_lay.addWidget(self.btn_veg)
        self.v_lay.addWidget(self.btn_drinks)
        self.v_lay.addWidget(self.btn_acc)
        self.v_lay.addWidget(self.btn_cart)
        self.v_lay.addWidget(self.btn_exit)

        self.setLayout(self.v_lay)

    def fruits(self):
        self.window = FruitsWindow(self)
        self.window.show()
        self.hide()

    def veg(self):
        self.window = VegetablesWindow(self)
        self.window.show()
        self.hide()

    def drinks(self):
        self.window = DrinksWindow(self)
        self.window.show()
        self.hide()

    def acc(self):
        self.window = AccessoriesWindow(self)
        self.window.show()
        self.hide()

    def cart_open(self):
        self.window = CartWindow(self)
        self.window.show()
        self.hide()


app = QApplication([])
window = MainWindow()
window.show()
app.exec_()