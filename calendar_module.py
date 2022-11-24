import calendar

def is_year_leap(year):
    if calendar.isleap(year) is True:
        return(f'\nThis year is leap year: {calendar.isleap(year)}')
        
    else:
        return(f'\nThis year is not leap year: {calendar.isleap(year)}')
        
year = int(input('Write a year to check is it leap: '))
print(is_year_leap(year))