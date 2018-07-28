import pymysql

class DBConnection():

    @staticmethod
    def getConnection():
        try:
            conn = pymysql.connect(host='localhost', user='root', password='', db='pizzapython')

            return conn
        except Exception as e:
            print(e)