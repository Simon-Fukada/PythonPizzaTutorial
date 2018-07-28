class PizzaToppings():

    def __init__(self, pizzaToppingID, typeID, sauce, meat, cheese, veggies):
        self.__pizzaToppingID = pizzaToppingID
        self.__typeID = typeID
        self.__sauce = sauce
        self.__meat = meat
        self.__cheeses = cheese
        self.__veggies = veggies

        # getters

    def getPizzaToppingID(self):
        return self.__pizzaToppingID

    def getTypeID(self):
        return self.__typeID

    def getSauce(self):
        return self.__sauce

    def getMeat(self):
        return self.__meat

    def getCheese(self):
        return self.__cheeses

    def getVeggies(self):
        return self.__veggies