import psycopg2
from data.config import POSTGRES_AUTH

# TODO: самодостаточный модуль, без глобалоk
class Sqlighter:

    def __init__(self, db_name):
        self.db_name = db_name

    def __enter__(self):
        self.connection = psycopg2.connect(user=POSTGRES_AUTH['user'],
                                  # пароль, который указали при установке PostgreSQL
                                  password=POSTGRES_AUTH['password'],
                                  host=POSTGRES_AUTH['host'],
                                  port=POSTGRES_AUTH['port'],
                                  database=self.db_name)
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()
        if exc_val:
            raise


class DatabaseConnection(Sqlighter): 
    
    def __init__(self, db_name: str, tables: list):
        self.db_name = db_name
        with Sqlighter(self.db_name) as connection:
            cursor = connection.cursor()
            self.create_tables(tables, multi=True)
            
    def create_tables(self, tables):
        with Sqlighter(self.db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(''.join(tables))

