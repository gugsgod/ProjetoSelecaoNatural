import mysql.connector

class Database:
    def login(self, db, user, password):
        mycursor = db.cursor(buffered=True)
        mycursor.execute("USE gamedb")
        mycursor.execute("SELECT * FROM users WHERE user = %s", [user])
        result = mycursor.fetchone()
        try:
            if result[0] is not None:
                if result[2] == password:
                    return True
                else:
                    return 'senha errada'
        except:
            return 'usuario nao existe'
            
    def register(self, db, user, password):
        mycursor = db.cursor(buffered=True)
        mycursor.execute("USE gamedb")
        mycursor.execute("SELECT max(id_user) FROM users")
        maxID = mycursor.fetchone()
        if maxID[0] == None:
            maxID = 1
        else:
            maxID = maxID[0] + 1
        try:
            mycursor.execute("INSERT INTO users VALUES (%s, %s, %s)", (maxID, user, password))
            db.commit()
        except Exception as error:
            return 'usuario ja existe'
        else:
            return 'criado'
            
    def insert_points(db, points, user):
        mycursor = db.cursor(buffered=True)
        mycursor.execute("USE gamedb")
        id_user = mycursor.execute("SELECT id_user FROM users WHERE user = %s", user)
        lap = mycursor.execute("SELECT max(lap) FROM points WHERE id_user = %s", id_user)
        if lap == None:
            lap = 1
        else:
            lap = lap[0] + 1
        mycursor.execute("INSERT INTO points VALUES (%s, %s, %s)", (id_user[0], points, lap))
        db.commit()
        
    def get_questions(self, mydb, question):
        mycursor = mydb.cursor(buffered=True)
        mycursor.execute("USE gamedb")
        mycursor.execute("SELECT * FROM questions WHERE id_question = %s", [question])
        return mycursor.fetchone()

    def get_top_5(self, mydb, idUser):
        mycursor = mydb.cursor(buffered=True)
        mycursor.execute("USE gamedb")
        mycursor.execute("SELECT score FROM points WHERE id_user = %s ORDER BY score DESC LIMIT 5", [idUser])
        return mycursor.fetchall()
    
    def get_id(self, mydb, email):
        mycursor = mydb.cursor(buffered=True)
        mycursor.execute("USE gamedb")
        mycursor.execute("SELECT id_user FROM users WHERE user = %s", [email])
        try:
            return mycursor.fetchone()[0]
        except TypeError:
            pass