from PyQt5.QtWidgets import *
import json

f = open("data.json", "r")
products = json.load(f)
f.close()


class FruitsWindow(QWidget):
    def __init__(self, main):
        super().__init__()

        self.main = main
        self.cart = main.cart

        self.setWindowTitle("Fruits")

        self.v_lay = QVBoxLayout()

        self.checks = []

        for name in products["Fruits"]:
            cb = QCheckBox(name + " - " + str(products["Fruits"][name]))
            self.checks.append((cb, name))
            self.v_lay.addWidget(cb)

        self.btn_add = QPushButton("Add")
        self.btn_menu = QPushButton("Menu")

        self.btn_add.clicked.connect(self.add)
        self.btn_menu.clicked.connect(self.menu)

        self.v_lay.addWidget(self.btn_add)
        self.v_lay.addWidget(self.btn_menu)

        self.setLayout(self.v_lay)

    def add(self):
        for cb, name in self.checks:
            if cb.isChecked():
                price = products["Fruits"][name]
                self.cart.append((name, price))
                cb.setChecked(False)

    def menu(self):
        self.main.show()
        self.close()