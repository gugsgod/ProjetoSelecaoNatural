import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "imtdb"
)

mycursor = mydb.cursor()

mycursor.execute("USE jogodb")

mycursor.execute("CREATE TABLE IF NOT EXISTS pontuação(id PRIMARY KEY, pontos INT, tentativa INT")

mycursor.execute("SHOW DATABASES")