import psycopg2
import os

connection = None
cursor = None


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


def init_db_students_table():
    # CREATE INIT TABLE WITH STUDENTS
    connection = create_db_connection()
    cursor = connection.cursor()

    # Check if there is table named Students and if there is not, create one
    cursor.execute(
        "SELECT * FROM information_schema.tables WHERE table_name=%s", ("students",)
    )
    if not bool(cursor.rowcount):
        cursor.execute(
            """CREATE TABLE STUDENTS(AIS_ID INT NOT NULL, SIMULATOR VARCHAR)"""
        )
        connection.commit()
    cursor.close()
    connection.close()
    
def insert_student(aisId:int, simulator:str):
    connection = create_db_connection()
    cursor = connection.cursor()
    cursor.execute(
            """INSERT INTO students (ais_id, simulator) VALUES (%s, %s)""",
            (
                aisId,
                simulator,
            ),
        )
    connection.commit()
    cursor.close()
    connection.close()
