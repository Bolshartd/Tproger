import calendar

def is_year_leap(year):
    if calendar.isleap(year) is True:
        print(f'\nThis year is leap: {calendar.isleap(year)}')
    else:
        print(f'\nThis year is not leap: {calendar.isleap(year)}')
is_year_leap(int(input('Write a year to check is it leap: ')))
