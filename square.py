# v1
import math

def square(a):
    perimeter = 4*a
    area = a**2
    diagonal = a*math.sqrt(2)
    return(f'Perimeter: {perimeter}, Area: {area}, Diagonal: {diagonal}')

a = int(input('Write a square side:'))
print(square(a))

#v2
# def square(a):
#     return (a*4, a**2, (2**0.5)*a)
# print(square(8))