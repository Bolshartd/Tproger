#interest rate a year -> 10%
def bank(cash, year):
    year_count = year/year 
    rate = int(cash*0.1) 
    profit = cash+rate 
    while year_count<=year:
        if year_count == year:
            print(f'Your profit for {year} years will be: {profit}')
        year_count += 1 
        b = int(profit*0.1) 
        profit += b 
    
full = bank(2000, 2)
