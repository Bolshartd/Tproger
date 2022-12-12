import random

def is_prime(i):
        if i == 0 or i ==2 or i ==3:
            return(f'{i} True')
        elif i%2 == 0 or i%3 == 0:
            return(f'{i} False')
        else:
            return(f'{i} True')
print(is_prime(random.randrange(0,1000)))