import sqlite3

DB_NAME = 'upx_schema.db'

class DatabaseConnection:
    def __init__(self, db_name=DB_NAME):
        self.db_name = db_name

    def get_connection(self):
        """Retorna uma nova conexão com o banco de dados."""
        return sqlite3.connect(self.db_name)

    def execute_query(self, query, params=()):
        """Executa uma query no banco de dados."""
        conn = None
        cursor = None
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()
            print("✅ Query executada com sucesso!")
        except sqlite3.Error as e:
            print(f"❌ SQLite error: {e}")
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def insert_sensor_data(self, data):
        """Insere dados do sensor no banco."""
        if not isinstance(data, dict):
            print("⚠️ Erro: Dados recebidos não são um dicionário válido.")
            return

        required_keys = {'sensor_id', 'temperature', 'humidity'}
        if not required_keys.issubset(data.keys()):
            print("⚠️ Erro: JSON recebido não tem todas as chaves necessárias.")
            return

        query = "INSERT INTO sensor_data (sensor_id, temperature, humidity) VALUES (?, ?, ?)"
        params = (1, data['temperature'], data['humidity'])
        self.execute_query(query, params)
        print(f"✅ Dados inseridos no banco: {data}")

# Instancia a conexão com o banco
dataBaseConnection = DatabaseConnection()