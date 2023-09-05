from typing import Union
import re

def re_standard_str(pattern: str, player_data: str) -> str:
    player_id = re.findall(pattern, player_data)
    return player_id[0]


def re_player_names_hof(pattern: str, player_data: str) -> tuple:
    names = re.findall(pattern, player_data)
    if not names or " " not in names[0]:
        return tuple()
    names = names[0].split()
    first_name = names[0]
    last_name = ' '.join(names[1:])
    hall_of_fame = "No"
    if "*" in last_name:
        last_name.replace("*", "")
        hall_of_fame = "Yes"

    return first_name, last_name, hall_of_fame
# ToDo: Fix Nene Issue


def re_standard_int(pattern: str, player_data: str) -> int:
    year = re.findall(pattern, player_data)[0]
    return int(year)


def re_height(pattern: str, player_data: str) -> float:
    height = re.findall(pattern, player_data)
    height = height[0].replace("-", ".")
    return float(height)


def re_dob(pattern: str, player_data: str) -> tuple:
    dob_combined = re.findall(pattern, player_data)
    if not dob_combined:
        return (0, 0, 0)
    year = dob_combined[0][:4]
    month = dob_combined[0][4:6]
    day = dob_combined[0][6:]

    return int(day), int(month), int(year)


def re_colleges(pattern: str, player_data: str):
    colleges = re.findall(pattern, player_data)
    if not colleges:
        return "None"
    return ', '.join(colleges)

def process_data(player_data: str) -> list:
    player_id = re_standard_str(r'csv=\"(\w+)\"', player_data)
    first_name, last_name, hall_of_fame = re_player_names_hof(r'html\">([a-zA-Z\s]+)<\/a>', player_data)
    from_year = re_standard_int(r'year_min\">([0-9]+)<\/td', player_data)
    to_year = re_standard_int(r'year_max\">([0-9]+)<\/td', player_data)
    seasons = (to_year - from_year) + 1
    position = re_standard_str(r'pos\">([A-Z-]+)<\/td>', player_data)
    height_ft = re_height(r'>([4-7]-[0-9]+)<\/td>', player_data)
    height_m = f"{height_ft / 3.288399}"[:4]
    weight_lbs = re_standard_int(r'\"weight\">([0-9\-]+)<\/td', player_data)
    weight_kg = int(weight_lbs * 0.45359237)
    dob_day, dob_month, dob_year = re_dob(r'csk=\"([0-9]+)\"', player_data)
    college = re_colleges(r'college=[a-z]+\">([\w\s]+)<\/a>', player_data)

    return [player_id, first_name, last_name, from_year, to_year, seasons, position, height_m, height_ft,
            weight_lbs, weight_kg, dob_day, dob_month, dob_year, college, hall_of_fame]



if __name__ == '__main__':

    p1 = '<tr><th class="left" data-append-csv="hachiru01" data-stat="player" scope="row"><strong><a href="/players/h/hachiru01.html">Rui Hachimura</a></strong></th><td class="right" data-stat="year_min">2020</td><td class="right" data-stat="year_max">2023</td><td class="center" data-stat="pos">F</td><td class="right" csk="80.0" data-stat="height">6-8</td><td class="right" data-stat="weight">230</td>' \
         '<td class="left" csk="19980208" data-stat="birth_date"><a href="/friv/birthdays.cgi?month=2&amp;day=8">February 8, 1998</a></td><td class="left" data-stat="colleges"><a href="/friv/colleges.fcgi?college=gonzaga">Gonzaga</a></td></tr>'
    [print(el) for el in process_data(p1)]

    p2 = '<tr data-row="36"><th scope="row" class="left " data-append-csv="hamiljo01" data-stat="player"><a href="/players/h/hamiljo01.html">Joe Hamilton</a></th><td class="right " data-stat="year_min">1971</td><td class="right " data-stat="year_max">1976</td><td class="center " data-stat="pos">G</td><td class="right " data-stat="height" csk="70.0">5-10</td><td class="right " data-stat="weight">160</td>' \
         '<td class="left " data-stat="birth_date" csk="19480705"><a href="/friv/birthdays.cgi?month=7&amp;day=5">July 5, 1948</a></td><td class="left " data-stat="colleges"><a href="/friv/colleges.fcgi?college=swchrist">Southwestern Christian College</a>, <a href="/friv/colleges.fcgi?college=ntexas">University of North Texas</a></td></tr>'
    [print(el) for el in process_data(p2)]

    # p3 = '<tr data-row="233"><th scope="row" class="left " data-append-csv="hilarne01" data-stat="player"><a href="/players/h/hilarne01.html">Nenê</a></th><td class="right " data-stat="year_min">2003</td><td class="right " data-stat="year_max">2019</td><td class="center " data-stat="pos">F-C</td><td class="right " data-stat="height" csk="83.0">6-11</td><td class="right " data-stat="weight">250</td><td class="left " data-stat="birth_date" csk="19820913"><a href="/friv/birthdays.cgi?month=9&amp;day=13">September 13, 1982</a></td><td class="left iz" data-stat="colleges"></td></tr>'
    # [print(el) for el in process_data(p3)]
