# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 07:49:15 2022

@author: FF246WR
"""
"""
What is function?
Funksiya - ma'lum bir kodlarning yig'indisi ya'ni bir necha qator kodlarning 
yig'indisi.

Why we need functions?
Dastur yozish jarayonida bir necha qator kodlarni takror-takror ishlatish
talab etilishi mumkin. Mana shunday holatlarda ularni qayta-qayta yozgandan
ko'ra, ularni bitta funksiyaga joylab qo'yishimiz mumkin.
"""

def say_hi(ism):
    """Foydalanuvchi ismini qabul qilib, 
    salom beruvchi funksiya""" # docstring
    print(f"Assalomu alaykum, hurmatli {ism.title()}!")

say_hi('doston')

# print(say_hi.__doc__)

# print(print.__doc__)


def yosh_hisobla(name, b_year):
    """Program that counts user's age"""
    print(f"{name.title()} is {2022-b_year} years old")

yosh_hisobla("Anvar", 1995)

yosh_hisobla(b_year=1995, name='olim')