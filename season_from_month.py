import calendar
def season(month):
    if month in ('December', 'January', 'February'):
        return ('Winter')
    elif month in ('March', 'April', 'May'):
        return ('Spring')
    elif month in ('June', 'July', 'August'):
        return ('Summer')
    elif month in ('September', 'October', 'November'):
        return ('Fall')

month = calendar.month_name[int(input("""Write a number from 1 to 12 to know what season is this month, where 1 -> January and 12 -> December\nNumber:"""))]
print(season(month))