import mysql.connector


class Database:
    def login(db, email, senha):
        database = db
        mycursor = database.cursor()
        mycursor.execute("USE jogodb")
        mycursor.execute("SELECT * FROM usuarios WHERE email = %s", email)
        result = mycursor.fetchone()
        if result[0] != None:
            if result[3] == senha:
                print("Email e senha estão corretos!")
            else:
                print("Deu merda, ta tudo errado!")
            
    def get_questions(db, question):
        database = db
        mycursor = database.cursor()
        mycursor.execute("USE jogodb")
        mycursor.execute("SELECT * FROM questoes WHERE idQuestao = %s", question)
        return mycursor.fetchone()
    
mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "imtdb"
    )    
    
db = Database

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "imtdb"
)

log = Database.login(mydb, ["gustavo@gmail.com"], "123321")
