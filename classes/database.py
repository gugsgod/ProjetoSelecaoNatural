import mysql.connector

class Database:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            print("Conexão estabelecida com sucesso!")
        except mysql.connector.Error as err:
            print("Erro ao conectar ao banco de dados:", err)

    def disconnect(self):
        if self.connection.is_connected():
            self.connection.close()
            print("Conexão encerrada.")

    def execute_query(self, query, values=None):
        cursor = self.connection.cursor()
        try:
            if values:
                cursor.execute(query, values)
            else:
                cursor.execute(query)
            self.connection.commit()
            print("Query executada com sucesso!")
        except mysql.connector.Error as err:
            print("Erro ao executar a query:", err)
        finally:
            cursor.close()
            
def criar_tabelas():
    # Conectar ao banco de dados
    conexao = mysql.connector.connect(
        host="localhost",
        user="seu_usuario",
        password="sua_senha",
        database="seu_banco_de_dados"
    )

    # Cursor para executar comandos SQL
    cursor = conexao.cursor()

    # Criar tabela 'cargos'
    cursor.execute("CREATE TABLE IF NOT EXISTS cargos (cargo INT PRIMARY KEY, nome_cargo VARCHAR(25))")

    # Criar tabela 'usuarios'
    cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (ID INT PRIMARY KEY AUTO_INCREMENT, nome VARCHAR(45), email VARCHAR(60), senha VARCHAR(16), cargo INT, FOREIGN KEY (cargo) REFERENCES cargos(cargo))")

    # Criar tabela 'pontuacao'
    cursor.execute("CREATE TABLE IF NOT EXISTS pontuacao (ID INT, pontos INT, vzsJogadas INT, FOREIGN KEY (ID) REFERENCES usuarios(ID))")

    # Criar tabela 'perguntas'
    cursor.execute("CREATE TABLE IF NOT EXISTS perguntas (NPergunta INT PRIMARY KEY, pergunta VARCHAR(300), a1 VARCHAR(160), a2 VARCHAR(160), a3 VARCHAR(160), a4 VARCHAR(160))")

    # Confirmar as alterações
    conexao.commit()

    # Fechar o cursor e a conexão
    cursor.close()
    conexao.close()

# Exemplo de uso:
db = Database(host="localhost", user="seu_usuario", password="sua_senha", database="seu_banco_de_dados")
db.connect()

# Exemplo de execução de uma query
query = "CREATE TABLE IF NOT EXISTS exemplo (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255))"
db.execute_query(query)

db.disconnect()