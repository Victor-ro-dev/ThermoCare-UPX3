import sqlite3
import json

DB_NAME = 'upx_schema.db'

class DatabaseConnection:
    def __init__(self, db_name=DB_NAME):
        """Define o nome do banco de dados."""
        self.db_name = db_name
    
    def execute_query(self, query, params=()):
        """Executa uma query no banco de dados."""
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute(query, params)
                conn.commit()  # Garante que os dados sejam salvos
                print("✅ Query executada com sucesso!")
        except sqlite3.Error as e:
            print(f"❌ SQLite error: {e}")
    
    def insert_sensor_data(self, data):
        """Insere dados do sensor no banco."""
        if not isinstance(data, dict):
            print("⚠️ Erro: Dados recebidos não são um dicionário válido.")
            return
        
        required_keys = {'temperatura', 'data', 'hora'}
        if not required_keys.issubset(data.keys()):
            print("⚠️ Erro: JSON recebido não tem todas as chaves necessárias.")
            return
        
        query = "INSERT INTO sensor_temp (temperatura, data, hora) VALUES (?, ?, ?)"
        params = (data['temperatura'], data['data'], data['hora'])
        self.execute_query(query, params)
        print(f"✅ Dados inseridos no banco: {data}")


# Instancia a conexão com o banco
dataBaseConnection = DatabaseConnection()


