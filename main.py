import sqlite3
import os
from web_scraping_script import extract_table_from_page
import db_controller
from process_raw_data import process_data


project_path = os.path.abspath(".")
db_path = os.path.join(project_path, "models", "nba_players_db.db")

conn = sqlite3.connect(db_path)
c = conn.cursor()
# c.execute("DROP TABLE players_bio")
# conn.commit()
c.execute("""CREATE TABLE players_bio (
                plid TEXT PRIMARY KEY,
                first_name TEXT,
                last_name TEXT,
                from_year INTEGER,
                to_year INTEGER,
                seasons INTEGER,
                position TEXT,
                height_m REAL,
                height_ft REAL,
                weight_kg INTEGER,
                weight_lbs INTEGER,
                dob_day INTEGER,
                dob_month TEXT,
                dob_year INTEGER,
                college TEXT,
                hall_of_fame TEXT)
""")

conn.commit()
# conn.close()

# player_data = ['KaAb47C225', 'Kareem', 'Abdul-Jabbar', 1970, 1989, 20, 'C', 2.18, 7.2, 102, 225, 16, 'April', 1947, 'UCLA', 'Yes']

# c.execute("""INSERT INTO players_bio VALUES ()""")


# SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}';

my_url = "https://www.basketball-reference.com/players/a/"
table = extract_table_from_page(my_url)

for row in table:
    if not row:
        break

    player_data = process_data(row)

    if len(player_data) != 16:
        db_controller.bad_data(player_data)
        continue

    print(player_data)
    c.execute(f"""INSERT INTO players_bio VALUES('{player_data[0]}', '{player_data[1]}', '{player_data[2]}', {player_data[3]},
                                                    {player_data[4]}, {player_data[5]}, '{player_data[6]}', {player_data[7]},
                                                    {player_data[8]}, {player_data[9]}, {player_data[10]}, {player_data[11]},
                                                    '{player_data[12]}', {player_data[13]}, '{player_data[14]}', '{player_data[15]}')""")

conn.commit()



