from process_raw_data import process_data
from web_scraping_script import extract_table_from_page

my_url = "https://www.basketball-reference.com/players/c/"
table = extract_table_from_page(my_url)

for row in table:
    player_data = process_data(row)
    print(player_data)
    break
