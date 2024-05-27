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
    pass