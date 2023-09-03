import os


def create_db(db_name) -> None:
    pass


def create_table(table_name) -> None:
    pass


def insert_values(db_name, table_name, player_data) -> None:
    pass


def delete_table(db_name, table_name) -> None:
    pass


def delete_db(db_name) -> None:
    pass


def bad_data(bad_row: str) -> None:
    project_path = os.path.abspath(".")
    bad_data_path = os.path.join(project_path, "models", "bad_data.txt")

    with open(bad_data_path, "a") as f:
        f.write(bad_row + "\n")
