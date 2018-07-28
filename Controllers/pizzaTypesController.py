import DBConnection as DB
from models import PizzaTypes as PT
from models import pizzaToppings as PTo

class pizzaTypesController():

    @staticmethod
    def getPizzaTypes():
        try:
            listOfPizzaTypes = []

            conn = DB.DBConnection.getConnection()
            cur = conn.cursor()
            cur.execute("SELECT * FROM pizzatypes")
            for row in cur:
                pizzaType = PT.PizzaTypes(row[0], row[1])#typeID, name
                listOfPizzaTypes.append(pizzaType)
            return listOfPizzaTypes
        except Exception as e:
            print(e)
        finally:
            conn.close()

    @staticmethod
    def getPizzaToppings(typeID):
        try:
            listOfPizzaToppings = []

            conn = DB.DBConnection.getConnection()
            cur = conn.cursor()
            cur.execute("SELECT * FROM pizzatoppings WHERE typeID = %s", (typeID))
            for row in cur:
                pizzaToppings = PTo.PizzaToppings(row[0], row[1], row[2], row[3], row[4], row[5])#pizzaToppingID, typeID, sauce, meat, cheese, veggies
                listOfPizzaToppings.append(pizzaToppings)
            return listOfPizzaToppings
        except Exception as e:
            print(e)
        finally:
            conn.close()