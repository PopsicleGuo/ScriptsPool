'''
 A small example for how to get datetime with python!
'''


from datetime import date


def get_weeknumber():
    weeknumber = date.today().isocalendar()[1]
    print("This week is: ", weeknumber)

# get_weeknumber()


def get_specificnumber(year, months, day):
    get_wknumber = date(int(year), int(months), int(day)).isocalendar()[1]
    print("This week number is: ", get_wknumber)

get_specificnumber(2018, 10, 1)