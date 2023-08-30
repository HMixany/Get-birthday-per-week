from datetime import date, datetime


def get_birthdays_per_week(users):
    result = {}
    days_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', "Friday"]

    today = date.today()
    delta = datetime(2023, 10, 10).date() - datetime(2023, 10, 3).date()
    final_date = today + delta

    for user in users:
        if today.year != final_date.year and user['birthday'].month == 1:
            curent = datetime(final_date.year, user['birthday'].month, user['birthday'].day).date()
        else:
            curent = datetime(today.year, user['birthday'].month, user['birthday'].day).date()

        if today <= curent < final_date:
            if curent.weekday() == 5 or curent.weekday() == 6:
                if result.get(days_week[0]) is None:
                    result[days_week[0]] = [(user['name'])]
                else:
                    result[days_week[0]].append(user['name'])
            else:
                if result.get(days_week[curent.weekday()]) is None:
                    result[days_week[curent.weekday()]] = [(user['name'])]
                else:
                    result[days_week[curent.weekday()]].append(user['name'])

    return result


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
