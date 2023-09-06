import os
import sqlite3


class DBClass:

    def __init__(self, db_name: str) -> None:
        self.db_name = db_name
        self.db_path = os.path.join(os.path.abspath("."), "models", db_name)
        self.connection = sqlite3.connect(self.db_path)
        self.cursor = self.connection.cursor()

    def create_table(self, table_name: str, table_properties: list) -> None:
        self.cursor.execute(f"""CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(table_properties)})""")
        self.connection.commit()
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

    def commit(self) -> None:
        self.connection.commit()

    def insert_values(self, table_name: str, values: list) -> None:
        self.cursor.execute(f"""INSERT INTO {table_name} VALUES (
        '{values[0]}', '{values[1]}', '{values[2]}', {values[3]},
        {values[4]}, {values[5]}, '{values[6]}', {values[7]},
        {values[8]}, {values[9]}, {values[10]}, {values[11]},
        '{values[12]}', {values[13]}, '{values[14]}', '{values[15]}')""")

    def delete_table(self, table_name) -> None:
        self.cursor.execute(f"""DROP TABLE IF EXISTS {table_name}""")
        self.connection.commit()
        # ToDo: create a log message after a table has been deleted

    def delete_db(self, db_name: str) -> None:
        pass
        # ToDo: delete file using os.remove("file.db")

    def close_connection(self) -> None:
        self.connection.close()

    @staticmethod
    def bad_data(bad_row: str) -> None:
        project_path = os.path.abspath(".")
        # File will be created inside project\models. Delete "models" if you want the file created in the main directory
        bad_data_path = os.path.join(project_path, "models", "bad_data.txt")

        with open(bad_data_path, "a") as f:
            f.write(bad_row + "\n")

if __name__ == '__main__':
    my_db = DBClass("db_test.db")
    my_db.create_table("test_table", ["first_column TEXT", "second_column INTEGER"])
    my_db.insert_values("test_table", ["test01", 1])
    my_db.insert_values("test_table", ["test02", 2])
    my_db.insert_values("test_table", ["test03", 2])
    # my_db.delete_table("test_table")
