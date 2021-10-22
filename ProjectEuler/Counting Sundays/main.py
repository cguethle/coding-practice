from datetime import date, timedelta


def get_number_of_sundays_easy(start_date, end_date=None):
    end_date = end_date or date.today()
    total = 0

    while start_date.weekday() != 6:
        start_date += timedelta(days=1)
    print(f"first sunday: {start_date}")

    while start_date <= end_date:
        print(f"checking date: {start_date}")
        if start_date.day == 1:
            total += 1
        start_date += timedelta(weeks=1)

    return total


if __name__ == "__main__":

    print(
        get_number_of_sundays_easy(
            date(year=1901, month=1, day=1),
            date(year=2000, month=12, day=31)
        )
    )
