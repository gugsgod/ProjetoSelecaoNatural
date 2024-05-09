import mysql.connector
    
class Database:
    def __init__(self):
        self.config={"user":'root', "password":'imtdb', "host":'localhost', "database": 'JogoDb'}
    def connect_to_db(self):
        try:
            cnx = mysql.connector.connect(**self.config)
            cursor = cnx.cursor()
            print("Connected to the database successfully!")
            return cnx, cursor
        except mysql.connector.Error as err:
            print(f"Error connecting to the database: {err}")
            return None, None
    def create_database(self, db_name):
        try:
            cnx, cursor = self.connect_to_db()
            if cnx is not None:
                cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
                cnx.commit()
                print(f"Database '{db_name}' created successfully!")
                return True
            else:
                print("Error: Unable to connect to the database.")
                return False
        except mysql.connector.Error as err:
            print(f"Error creating database: {err}")
            return False
    def check_table_exists(self, db_name, table_name):
        try:
            cnx, cursor = self.connect_to_db()
            if cnx is not None:
                cursor.execute(f"USE {db_name}")
                cursor.execute(f"SHOW TABLES LIKE '{table_name}'")
                result = cursor.fetchone()
                if result is not None:
                    return True
                else:
                    return False
            else:
                print("Error: Unable to connect to the database.")
                return False
        except mysql.connector.Error as err:
            print(f"Error checking table existence: {err}")
            return False
    def create_table(self, db_name, table_name, columns):
        try:
            cnx, cursor = self.connect_to_db()
            if cnx is not None:
                cursor.execute(f"USE {db_name}")
                cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})")
                cnx.commit()
                print(f"Table '{table_name}' created successfully!")
                return True
            else:
                print("Error: Unable to connect to the database.")
                return False
        except mysql.connector.Error as err:
            print(f"Error creating table: {err}")
            return False
    def pull_data(self, db_name, table_name, columns):
        try:
            cnx, cursor = self.connect_to_db()
            if cnx is not None:
                cursor.execute(f"USE {db_name}")
                cursor.execute(f"SELECT {columns} FROM {table_name}")
                result = cursor.fetchall()
                return result
            else:
                print("Error: Unable to connect to the database.")
                return None
        except mysql.connector.Error as err:
            print(f"Error pulling data: {err}")
            return None
    def pull_table(self, db_name, table_name):
        try:
            cnx, cursor = self.connect_to_db()
            if cnx is not None:
                cursor.execute(f"USE {db_name}")
                cursor.execute(f"SELECT * FROM {table_name}")
                result = cursor.fetchall()
                return result
            else:
                print("Error: Unable to connect to the database.")
                return None
        except mysql.connector.Error as err:
            print(f"Error pulling table: {err}")
            return None
    def insert_data(self, db_name, table_name, data):
        try:
            cnx, cursor = self.connect_to_db()
            if cnx is not None:
                cursor.execute(f"USE {db_name}")
                cursor.executemany(f"INSERT INTO {table_name} VALUES (%s)", data)
                cnx.commit()
                print(f"Data inserted successfully into table '{table_name}'!")
                return True
            else:
                print("Error: Unable to connect to the database.")
                return False
        except mysql.connector.Error as err:
            print(f"Error inserting data: {err}")
            return False
    
db = Database()
db.connect_to_db()