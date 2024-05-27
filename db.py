import psycopg2 as psql

class Database:
    @staticmethod
    def connect(query, query_type):
        db = psql.connect(
            database="test",
            host="localhost",
            user="postgres",
            password="example_pass"
        )

class Model:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
