# calling module
from prettytable import PrettyTable 
# adding the hat of the table with data
phone_table = PrettyTable(["Phone", "Color", "Price"])
# adding rows with data
phone_table.add_row(["Iphone", "Red", "46200"])
phone_table.add_row(["Samsung", "White", "52800"])
phone_table.add_row(["Sony", "Black", "49900"])
phone_table.add_row(["Honor", "Yellow", "50000"])

print(phone_table)