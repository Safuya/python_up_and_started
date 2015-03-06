from datetime import date
from datetime import time
from datetime import datetime


def main():
    today = date.today()
    print("Todays date is", today)
    print("Date components:", today.day, today.month, today.year)
    print("Todays weekday:", today.weekday())

    today = datetime.now()
    print("The current date and time is", today)

    current_time = datetime.time(datetime.now())
    print("The current time is", current_time)

    wd = date.weekday(today)
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    print("Today is day number %d" % wd)
    print("Which is a", days[wd])


if __name__ == "__main__":
    main()
