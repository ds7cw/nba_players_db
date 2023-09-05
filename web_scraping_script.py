import requests
from bs4 import BeautifulSoup


def extract_table_from_page(page_url: str):

    r = requests.get(page_url)
    soup_result = BeautifulSoup(r.text, features="html.parser")
    table_container = soup_result.find("tbody").find_all("tr")

    return table_container


if __name__ == '__main__':
    my_url = "https://www.basketball-reference.com/players/h/"
    [print(row) for row in extract_table_from_page(my_url)]
