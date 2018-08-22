from datetime import date


def get_weeknumber():
    today = date.today()
    weeknumber = today.isocalendar()[1]
    print("This week is: ", weeknumber)

# get_weeknumber()


def get_specificnumber(year, months, day):
    get_format = date(int(year), int(months), int(day))
    get_wknumber = get_format.isocalendar()[1]
    print("This week number is: ", get_wknumber)

get_specificnumber(2018, 10, 1)