from datetime import datetime, timedelta


def current_datetime():
    return datetime.now()


def add_days(days):
    return datetime.now() + timedelta(days=days)


def date_difference(date1, date2):
    return abs((date2 - date1).days)


def format_date(date):
    return date.strftime("%Y-%m-%d %H:%M:%S")


if __name__ == "__main__":
    now = current_datetime()
    print(format_date(now))
    future = add_days(7)
    print(format_date(future))
    print(date_difference(now, future))