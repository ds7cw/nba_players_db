import os
import sqlite3


def connect_to_db(db_name: str) -> sqlite3.Connection:
    project_path = os.path.abspath(".")
    # File will be created inside project\models. Delete "models" if you want the file created in the main directory
    db_path = os.path.join(project_path, "models", db_name)

    db_connection = sqlite3.connect(db_path)
    return db_connection

def commit_to_db(conn: sqlite3.Connection) -> None:
    conn.commit()


def close_connection_to_db(conn: sqlite3.Connection) -> None:
    conn.close()


def create_table(cursor: sqlite3.Cursor, table_name: str, table_properties: list) -> None:
    cursor.execute(f"""CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(table_properties)})""")

    #                   plid TEXT PRIMARY KEY,
    #                     first_name TEXT,
    #                     last_name TEXT,
    #                     from_year INTEGER,
    #                     to_year INTEGER,
    #                     seasons INTEGER,
    #                     position TEXT,
    #                     height_m REAL,
    #                     height_ft REAL,
    #                     weight_kg INTEGER,
    #                     weight_lbs INTEGER,
    #                     dob_day INTEGER,
    #                     dob_month TEXT,
    #                     dob_year INTEGER,
    #                     college TEXT,
    #                     hall_of_fame TEXT


def insert_values(cursor: sqlite3.Cursor, table_name: str, player_data: list) -> None:
    cursor.execute(f"""INSERT INTO {table_name} VALUES (
    '{player_data[0]}', '{player_data[1]}', '{player_data[2]}', {player_data[3]},
    {player_data[4]}, {player_data[5]}, '{player_data[6]}', {player_data[7]},
    {player_data[8]}, {player_data[9]}, {player_data[10]}, {player_data[11]},
    '{player_data[12]}', {player_data[13]}, '{player_data[14]}', '{player_data[15]}')""")


def delete_table(cursor: sqlite3.Cursor, table_name: str) -> None:
    cursor.execute(f"DROP TABLE {table_name}")
    # ToDo: create a log message after a table has been deleted


def delete_db(db_name: str) -> None:
    pass
    # ToDo: delete file using os.remove("file.db")


def bad_data(bad_row: str) -> None:
    project_path = os.path.abspath(".")
    # File will be created inside project\models. Delete "models" if you want the file created in the main directory
    bad_data_path = os.path.join(project_path, "models", "bad_data.txt")

    with open(bad_data_path, "a") as f:
        f.write(bad_row + "\n")
