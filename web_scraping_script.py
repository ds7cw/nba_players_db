import requests
from bs4 import BeautifulSoup


def extract_table_from_page(page_url: str) -> list:

    r = requests.get(page_url)
    soup_result = BeautifulSoup(r.text, features="html.parser")
    table_container = soup_result.find("div", class_ = "table_container").text
    split_table = table_container.split("\n")

    for idx, row in enumerate(split_table):
        if row == "Colleges":
            return split_table[idx + 3:]


if __name__ == '__main__':
    my_url = "https://www.basketball-reference.com/players/h/"
    [print(row) for row in extract_table_from_page(my_url)]
