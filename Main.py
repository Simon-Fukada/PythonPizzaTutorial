from PyQt5 import QtWidgets, uic
from Controllers import pizzaTypesController as PTC
class MyWindow(QtWidgets.QMainWindow):

    listOfPizzas = []

    def __init__(self):
        super(MyWindow, self).__init__()
        uic.loadUi('orderAPizza.ui',self)
        self.init()

    def init(self):
        global listOfPizzas
        listOfPizzas = PTC.pizzaTypesController.getPizzaTypes()

        for x in listOfPizzas:
            self.cbPizzaTypes.addItem(x.getName())

        self.twPizzaToppings.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem("Sauce"))
        self.twPizzaToppings.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem("Meat"))
        self.twPizzaToppings.setHorizontalHeaderItem(2, QtWidgets.QTableWidgetItem("Cheese"))
        self.twPizzaToppings.setHorizontalHeaderItem(3, QtWidgets.QTableWidgetItem("Veggies"))

        self.lbOrdered.hide()

        self.cbPizzaTypes.currentIndexChanged.connect(self.pizzaSelected)
        self.btnOrder.clicked.connect(self.order)

        self.pizzaSelected()

    def pizzaSelected(self):
        try:
            cbPizzaIndex = self.cbPizzaTypes.currentIndex()
            selectedPizza = listOfPizzas[cbPizzaIndex]
            pizzaTypeID = selectedPizza.getTypeID()

            listOfPizzaToppings = PTC.pizzaTypesController.getPizzaToppings(pizzaTypeID)

            self.twPizzaToppings.setRowCount(0)
            for row_number, row_data in enumerate(listOfPizzaToppings):
                self.twPizzaToppings.insertRow(row_number)
                self.twPizzaToppings.setItem(row_number, 0, QtWidgets.QTableWidgetItem(row_data.getSauce()))
                self.twPizzaToppings.setItem(row_number, 1, QtWidgets.QTableWidgetItem(row_data.getMeat()))
                self.twPizzaToppings.setItem(row_number, 2, QtWidgets.QTableWidgetItem(row_data.getCheese()))
                self.twPizzaToppings.setItem(row_number, 3, QtWidgets.QTableWidgetItem(row_data.getVeggies()))
        except Exception as e:
            print(e)

    def order(self):
        self.lbOrderStatus.hide()
        self.lbOrdered.show()


def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()