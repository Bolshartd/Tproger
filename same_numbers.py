numbers = 1, 4, 6, 7, 8, 99, 61, 34

def all_unique(numbers):
    return len(numbers) == len(set(numbers))
print (all_unique(numbers))
