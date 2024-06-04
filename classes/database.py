import mysql.connector

class Database:
    def login(db, email, senha):
        mycursor = db.cursor()
        mycursor.execute("USE jogodb")
        mycursor.execute("SELECT * FROM usuarios WHERE email = %s", email)
        result = mycursor.fetchone()
        try:
            if result[0] is not None:
                if result[3] == senha:
                    print("Email e senha estão corretos!")
                else:
                    print("Senha incorreta!")
        except:
            print("Conta com esse email não existe")
            
    def register(db, nome, email, senha):
        mycursor = db.cursor()
        mycursor.execute("USE jogodb")
        mycursor.execute("SELECT max(idUsuario) FROM usuarios")
        maxID = mycursor.fetchone()
        maxID = maxID[0] + 1
        try:
            mycursor.execute("INSERT INTO usuarios VALUES (%s, %s, %s, %s, 1)", (maxID, nome, email, senha))
            db.commit()
        except mysql.connector.errors.IntegrityError:
            print("Email já cadastrado")
            
    def insert_points(db, pontos, email):
        mycursor = db.cursor()
        mycursor.execute("USE jogodb")
        usuario = mycursor.execute("SELECT idUsuario FROM usuarios WHERE email = %s", email)
        print(usuario)
        rodada = mycursor.execute("SELECT max(rodada) FROM pontuacao WHERE idUsuario = %s", usuario)
        if rodada == None:
            rodada = 1
        else:
            rodada = rodada[0] + 1
        print(rodada)
        mycursor.execute("INSERT INTO pontuacao VALUES (%s, %s, %s)", (usuario[0], pontos, rodada))
        db.commit()
        
    def get_questions(db, question):
        mycursor = db.cursor()
        mycursor.execute("USE jogodb")
        mycursor.execute("SELECT * FROM questoes WHERE idQuestao = %s", question)
        return mycursor.fetchone()
