import calendar

calendar = calendar.month(2022, 7)
print(calendar)
def date(year, month, day):
    if str(year) in calendar and str(month) in calendar and str(day) in calendar:
        return('True')
    else:
        return('False')

print(date(2022, 'July', 31))
