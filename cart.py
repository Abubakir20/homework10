from PyQt5.QtWidgets import *


class CartWindow(QWidget):
    def __init__(self, main):
        super().__init__()

        self.main = main
        self.cart = main.cart

        self.setWindowTitle("Cart")

        self.v_lay = QVBoxLayout()

        self.list = QListWidget()
        self.total = QLabel()

        self.btn_buy = QPushButton("Buy all")
        self.btn_clear = QPushButton("Clear")
        self.btn_menu = QPushButton("Menu")

        self.btn_buy.clicked.connect(self.buy)
        self.btn_clear.clicked.connect(self.clear)
        self.btn_menu.clicked.connect(self.menu)

        self.v_lay.addWidget(self.list)
        self.v_lay.addWidget(self.total)
        self.v_lay.addWidget(self.btn_buy)
        self.v_lay.addWidget(self.btn_clear)
        self.v_lay.addWidget(self.btn_menu)

        self.setLayout(self.v_lay)

        self.update()

    def update(self):
        self.list.clear()

        total = 0

        for name, price in self.cart:
            self.list.addItem(name + " - " + str(price))
            total += price

        self.total.setText("Total: " + str(total))

    def buy(self):
        if len(self.cart) == 0:
            QMessageBox.warning(self, "Error", "Cart is empty!")
            return

        total = 0
        for name, price in self.cart:
            total += price

        QMessageBox.information(
            self,
            "Payment",
            "Siz " + str(total) + " so'm to'ladingiz!\nHaridingiz uchun rahmat!"
        )

        self.cart.clear()
        self.update()

    def clear(self):
        self.cart.clear()
        self.update()

    def menu(self):
        self.main.show()
        self.close()