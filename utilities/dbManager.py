import mysql.connector


def createDbConnection():
    global mydb
    mydb = mysql.connector.connect(

        host="localhsot",
        user="root",
        password="selenium",
        database="pydb"

    )


def getMysqlQuery(query):
    mycusor = mydb.cursor()
    mycusor.execute(query)
    myresult = mycusor.fetchone()
    return myresult[0]
