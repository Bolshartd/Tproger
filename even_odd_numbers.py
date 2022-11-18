# Even and odd numbers.If number 237 - stop.
my_list = [1, 34, 268, 34, 534, 85, 113, 237, 340, 515, 90]

def numbers(my_list):
    for i in my_list:
        if i == 237:
            break
        elif i%2 == 0:
            print (f'even number:{i}')
        else:
            print (f'odd number:{i}')
    else:
        i = i+1
numbers (my_list)