from PyQt5.QtWidgets import *
import json

f = open("data.json", "r")
products = json.load(f)
f.close()


class VegetablesWindow(QWidget):
    def __init__(self, main):
        super().__init__()

        self.main = main
        self.cart = main.cart

        self.setWindowTitle("Vegetables")

        self.v_lay = QVBoxLayout()
        self.checks = []

        for name in products["Vegetables"]:
            cb = QCheckBox(name + " - " + str(products["Vegetables"][name]))
            self.checks.append((cb, name))
            self.v_lay.addWidget(cb)

        btn_add = QPushButton("Add")
        btn_menu = QPushButton("Menu")

        btn_add.clicked.connect(self.add)
        btn_menu.clicked.connect(self.menu)

        self.v_lay.addWidget(btn_add)
        self.v_lay.addWidget(btn_menu)

        self.setLayout(self.v_lay)

    def add(self):
        for cb, name in self.checks:
            if cb.isChecked():
                price = products["Vegetables"][name]
                self.cart.append((name, price))
                cb.setChecked(False)

    def menu(self):
        self.main.show()
        self.close()