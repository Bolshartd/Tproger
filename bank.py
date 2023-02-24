#v1
def bank(cash, year):
    year_count = year/year 
    rate = int(cash*0.1) #interest rate a year -> 10%
    profit = cash+rate 
    while year_count <= year:
        if year_count == year:
            print(f'Your profit for {year} years will be: {profit}')
        year_count += 1 
        b = int(profit*0.1) 
        profit += b 


full = bank(2000, 2)

# #v2
# class Start_stack:
#     def __init__(self, cash, year):
#         self.cash = cash
#         self.year = year
    
# class Profit:
#     def __init__(self, cash, year):
#         self.perc = int(full.cash*0.1) #interest rate a year -> 10%
#         self.cash = full.cash+self.perc 
#         self.year_count = full.year/full.year 
#         while self.year_count < full.year:
#             if self.year_count == full.year:
#                 print(f'Your profit for {year} years will be: {self.cash}')
#             self.year_count += 1 
#             self.perc = int(self.cash*0.1) 
#             self.cash += self.perc 
            
# full = Start_stack(1000, 5)
# percent = Profit(full.cash, full.year)
