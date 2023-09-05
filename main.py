from web_scraping_script import extract_table_from_page
import db_controller
from process_raw_data import process_data
import time


db_connection = db_controller.connect_to_db("nba_players_db.db")
db_cursor = db_connection.cursor()

# db_connection.commit()
table_params = ["plid TEXT PRIMARY KEY", "first_name TEXT", "last_name TEXT", "from_year INTEGER",
                "to_year INTEGER", "seasons INTEGER", "position TEXT", "height_m REAL", "height_ft REAL",
                "weight_kg INTEGER", "weight_lbs INTEGER", "dob_day INTEGER", "dob_month TEXT", "dob_year INTEGER",
                "college TEXT", "hall_of_fame TEXT"]

# Create Table
players_bio_table_name = "players_bio"
db_controller.create_table(db_cursor, players_bio_table_name, table_params)
db_controller.commit_to_db(db_connection)

# db_connection.close()

# Test with a single row
# player_data = ['KaAb47C225', 'Kareem', 'Abdul-Jabbar', 1970, 1989, 20, 'C', 2.18, 7.2, 102, 225, 16, 'April', 1947, 'UCLA', 'Yes']
# db_controller.insert_values(db_cursor, players_bio_table_name, player_data)
# db_controller.commit_to_db(db_connection)

letters = "abcdefghijklmnopqrstuvwxyz"

for character in letters:

    my_url = f"https://www.basketball-reference.com/players/{character}/"
    table = extract_table_from_page(my_url)

    for row in table:

        try:
            player_data = process_data(str(row))

            # if len(player_data) != 16:
            #     db_controller.bad_data(row)
            #     continue
        except:
            # db_controller.bad_data(row)
            continue

        print(player_data)

        db_controller.insert_values(db_cursor, players_bio_table_name, player_data)

    time.sleep(15)

db_controller.commit_to_db(db_connection)
db_controller.close_connection_to_db(db_connection)

# SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}';
