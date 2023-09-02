def process_data(player_data: str) -> list:

    idx = [i for i in range(len(player_data)) if player_data[i].isdigit()][0]
    first_name, last_name = player_data[:idx].split()

    hall_of_famer = "No"
    if last_name[-1] == "*":
        hall_of_famer = "Yes"
        last_name = last_name[:-1]

    from_year, to_year = player_data[idx:idx + 4], player_data[idx + 4: idx + 8]
    seasons_played = int(to_year) - int(from_year) + 1

    pos_idx = idx + 8
    position = player_data[pos_idx]

    dob_m_idx = [i for i in range(pos_idx + 1, len(player_data)) if player_data[i].isalpha()][0]
    weight_lbs = player_data[dob_m_idx - 3: dob_m_idx]
    weight_kg = int(float(weight_lbs) * 0.45359237)

    ft, inches = player_data[pos_idx + 1:dob_m_idx - 3].split("-")
    height_ft = f"{ft}.{inches}"
    height_m = f"{float(height_ft) / 3.288399}"[:4]

    dob_month, dob_day, dob_year_college, *args = player_data[dob_m_idx:].split()
    dob_day = dob_day[:-1]
    dob_year, college = dob_year_college[:4], dob_year_college[4:]
    if args:
        college = ' '.join([college] + args)

    return [first_name, last_name, from_year, to_year, seasons_played, position, height_m,
            height_ft, weight_kg, weight_lbs, dob_day, dob_month, dob_year, college, hall_of_famer]


if __name__ == '__main__':
    my_player = "Kareem Abdul-Jabbar*19701989C7-2225April 16, 1947UCLA"
    [print(field) for field in process_data(my_player)]

    # Test with long college name
    p2 = "Joe Hamilton19711976G5-10160July 5, 1948Southwestern Christian College, University of North Texas"
    [print(field) for field in process_data(p2)]
