# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 12:42:14 2022

@author: FF246WR
"""

# =============================================================================
# numb = 1
# while numb <= 5:
#     print(numb, end=' ')
#     numb += 1
# print('Program finished!')
# 
# print('A program that returns a squre of a number')
# prompt = "Enter any value! "
# prompt += "(to stop the program, write 'exit'!): "
# value = ''
# while value != 'exit':
#     value = input(prompt)
#     if value != 'exit':
#         print(float(value)**2)
# print('Program finished!')
# =============================================================================


# =============================================================================
# print('A program that returns a squre of a number')
# prompt = "Enter any value! "
# prompt += "(to stop the program, write 'exit'!): "
# flag = True
# while flag:
#     value = input(prompt)
#     if value == 'exit':
#         flag = False
#     else:
#         print(float(value)**2)
# print('Program finished!')
# =============================================================================


# =============================================================================
# print('A program that returns a squre of a number')
# prompt = "Enter any value! "
# prompt += "(to stop the program, write 'exit'!): "
# 
# while True:  # abadiy sikl/ infinite loop
#     value = input(prompt)
#     if value == 'exit':
#         break # siklni to'xtatish
#     else:
#         print(float(value)**2)
# print('Program finished!')
# =============================================================================


# =============================================================================
# numbers = list(range(1, 11))
# for numb in numbers:
#     if numb == 5:
#         break
#     print(f"{numb} ning kvadrati {numb**2} ga teng")
# 
#     
# # Continue
# numbers = list(range(1, 11))
# for numb in numbers:
#     if numb == 5:
#         continue
#     print(f"{numb} ning kvadrati {numb**2} ga teng")
# =============================================================================

son = 0
while son < 10:
    son += 1
    if son % 2 != 0:
        continue
    else:
        print(son)

