import psycopg2
import os

def create_db_connection(db_name: str = None):
    db_name = db_name or os.getenv("DATABASE_NAME")

    # establishing the connection
    conn = psycopg2.connect(
        database=db_name,
        user=os.getenv("DATABASE_USER"),
        password=os.getenv("DATABASE_PASSWORD"),
        host=os.getenv("DATABASE_HOST"),
        port=os.getenv("DATABASE_PORT"),
    )
    return conn


def close_db_connection(cursor, connection):
    cursor.close()
    connection.close()

def execute_query(query, arguments=None):
    connection = create_db_connection()
    cursor = connection.cursor()
    if not arguments:
        cursor.execute(query)
    else:
        cursor.execute(query,arguments)
    result = cursor.fetchall()
    connection.commit()
    close_db_connection(cursor, connection)
    return result

