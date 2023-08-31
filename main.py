from datetime import date, datetime, timedelta


def get_birthdays_per_week(users):
    result = {}
    today = date.today()
    final_date = today + timedelta(weeks=1)

    for user in users:
        if today.year != final_date.year and user['birthday'].month == 1:
            curent = datetime(final_date.year, user['birthday'].month, user['birthday'].day).date()
        else:
            curent = datetime(today.year, user['birthday'].month, user['birthday'].day).date()

        if today <= curent < final_date:
            if curent.strftime('%A') in ('Saturday', 'Sunday'):
                if today.strftime('%A') == 'Monday':
                    continue
                if 'Monday' in result:
                    result['Monday'].append(user['name'])
                else:
                    result['Monday'] = [(user['name'])]
            else:
                if curent.strftime('%A') in result:
                    result[curent.strftime('%A')].append(user['name'])
                else:
                    result[curent.strftime('%A')] = [(user['name'])]

    return result


def result_output(result):
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    result_output(result)