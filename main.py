import time
from web_scraping_script import extract_table_from_page
import db_controller
from process_raw_data import process_data


# Create Database
my_db = db_controller.DBClass("nba_players_db.db")

# Create Table
players_bio_table_name = "players_bio"

table_params = ["plid TEXT PRIMARY KEY", "first_name TEXT", "last_name TEXT", "from_year INTEGER",
                "to_year INTEGER", "seasons INTEGER", "position TEXT", "height_m REAL", "height_ft REAL",
                "weight_kg INTEGER", "weight_lbs INTEGER", "dob_day INTEGER", "dob_month TEXT", "dob_year INTEGER",
                "college TEXT", "hall_of_fame TEXT"]

my_db.create_table(players_bio_table_name, table_params)

letters = "abcdefghijklmnopqrstuvwxyz"

for character in letters:

    my_url = f"https://www.basketball-reference.com/players/{character}/"
    table = extract_table_from_page(my_url)

    for row in table:

        try:
            player_data = process_data(str(row))
            print(player_data)
            my_db.insert_values(players_bio_table_name, player_data)

        except:
            my_db.bad_data(str(row))
            continue

    time.sleep(2)

my_db.commit()
my_db.close_connection()
