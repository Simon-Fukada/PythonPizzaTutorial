class PizzaTypes():


    def __init__(self, typeID, name):#constructor
        self.__typeID = typeID
        self.__name = name



    #setters
    def setName(self, name):
        self.__name = name

    #Getters
    def getTypeID(self):
        return self.__typeID

    def getName(self):
        return self.__name
