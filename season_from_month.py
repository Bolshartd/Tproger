import calendar
def season(month):
    if (month == 'December') or (month == 'January') or (month == 'February'):
        return ('Winter')
    elif (month == 'March') or (month == 'April') or (month == 'May'):
        return ('Spring')
    elif (month == 'June') or (month == 'July') or (month == 'August'):
        return ('Summer')
    elif (month == 'September') or (month == 'October') or (month == 'November'):
        return ('Fall')

month = calendar.month_name[int(input("""Write a number from 1 to 12, where 1 -> January and 12 -> December\nNumber:"""))]
print(season(month))