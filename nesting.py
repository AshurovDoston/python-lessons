# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 08:59:28 2022

@author: FF246WR
"""
# =============================================================================
# 
# car0 = {
#         'model':'gentra',
#         'rang':'qora',
#         'yil':2020,
#         'narx':15000,
#         'km':20000,
#         'korobka':'avtomat'
#         }
# 
# car1 = {
#         'model':'spark',
#         'rang':'oq',
#         'yil':2019,
#         'narx':8000,
#         'km':30000,
#         'korobka':'mexanika'
#         }
# 
# car2 = {
#         'model':'cobalt',
#         'rang':'mokriy',
#         'yil':2022,
#         'narx':14000,
#         'km':10000,
#         'korobka':'avtomat'
#         }
# 
# cars = [car0, car1, car2]
# for car in cars:
#     print(
#         f"{car['model'].title()}, "
#         f"{car['rang']} rang, "
#         f"{car['yil']}-yil, {car['narx']}$"
#           )
#     
#     
# =============================================================================

# =============================================================================
# # Bo'sh ro'yxatlardan for sikli yordamida to'la ro'yxat yaratish
# malibus = []
# for n in range(10):
#     new_car = {
#         'model':'malibu',
#         'rang':None, # rangi hali noaniq
#         'yil':2022,
#         'narx':None,
#         'km':0,
#         'korobka':'avtomat'
#         }
#     malibus.append(new_car)
# 
# for malibu in malibus[:3]:
#     malibu['rang']='qora'
#     
# for malibu in malibus[3:6]:
#     malibu['rang']='oq'
#     
# for malibu in malibus[6:]:
#     malibu['rang']='mokriy'
#     malibu['korobka']='mexanika'
# 
# 
# for malibu in malibus:
#     if malibu['korobka']=='avtomat':
#         malibu['narx']=40000
#     else:
#         malibu['narx']=35000
#         
# for malibu in malibus:
#     print(malibu)
#     
# =============================================================================


# Lug'at ichida ro'yxat

programmers = {
    'ali':['python', 'c++'],
    'vali':['html', 'css', 'js'],
    'hasan':['php', 'sql'],
    'husan':['python', 'php'],
    'maryam':['c++', 'c#']
    }

for name, langs in programmers.items():
    print(f"\n{name.title()} knows below languages:")
    for lang in langs:
        print(f"{lang.upper()} ", end=' ')