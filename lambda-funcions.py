from logging import root
import math

# lambda function - only consists of one line

circumference = lambda pi, r : 2 * pi * r
print(circumference(math.pi, 10))

square = lambda x, y : x ** y
print(square(4, 2))


## biz daraja funksiyasi orqali istalgan sonning darajasini hisoblaydigan boshqa bir funksiya yarata olamiz, lambda funksiya sharofati bilan
def daraja(n):
    return lambda x : x ** n 

## Istalgan sonning kvadratini hisoblaydigan funksiya. Bu yerda n = 2
kvadrat = daraja(2)
print(kvadrat(5))

## n = 3
kub = daraja(3)
print(f"4 ning kubi {kub(4)} ga teng")



### map funksiyasi
from math import sqrt
numbers = list(range(11))
## Map funksiyasi ishlashi: numbers ro'yxatini oladi va uning har bir elementi uchun sqrt funksiyasini qo'llaydi (below)
roots = list(map(sqrt, numbers))
print(roots)


### Below the long code is the same with the upper one which we use there map function
print("manual")
ildizlar = []
for numb in numbers:
    ildizlar.append(sqrt(numb))

print(ildizlar)



## Ro'yxat ichidagi sonlar kvadratini chiqarish 
def daraja2(x):
    return x*x

kvadrat = list(map(daraja2, numbers))
print(kvadrat)

## the same with the above one which we created longer def function. Here with the help of lambda function, implementing it so easy and readable
kvadratlar = list(map(lambda x : x*x, numbers))
print(kvadratlar)

a = [4, 6, 12]
b = [11, 7, 9]
a_plus_b = list(map(lambda x, y : x + y, a, b))
print(a_plus_b)


import random as r
sonlar = r.sample(range(100), 10)
print(sonlar)

# def juftmi(x):
#     """x juft bo'lsa True, aks holda False qaytaradi"""
#     return x%2 == 0

# n = 90
# print(f"{n} soni juftmi {juftmi(n)}")

# ## filter funksiyasi xuddi map funksiyasiga o'xshab bitta funksiya va ro'yxat qabul qiladi
# juft_sonlar = list(filter(juftmi, sonlar))
# print(juft_sonlar)

### the above function with lamba
juft_sonlar = list(filter(lambda x: x % 2 == 0, sonlar))
print(juft_sonlar)

fruits = ['banana', 'apple', 'melon', 'babaco', 'peach', 'apricot', 'bacuri']
letter = 'b'
fruits_b = list(filter(lambda fruit : fruit.startswith(letter), fruits))
print(fruits)
print(fruits_b)

fruits2 = list(filter(lambda fruit : len(fruit)<6, fruits))
print(fruits2)