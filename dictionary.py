# =============================================================================
# car_0 = {'model':'ferrari', 'colour':'red'}
# print(car_0['model'])
# 
# mevalar = {'olma':10000, 'tarvuz':8000, 'shaftoli':12000, 'qovun':11000}
# print(mevalar['olma'])
# print(f"Tarvuz narxi {mevalar['tarvuz']} so'm")
# 
# =============================================================================
student_0 = {
    'name':'murod olimov',
    'age':22,
    'birth_year':2022
    }

# =============================================================================
# print(f"{student_0['name'].title()} \
#       {student_0['birth_year']}-yilda tug'ilgan, \
#     {student_0['age']} yoshda")
# =============================================================================

student_0['course'] = 4
student_0['faculty'] = 'Computer Science'
student_0['name'] = 'abdulloh'

# Empty dictionary
student_1 = {}
student_1['name'] = 'ismoil'
student_1['course'] = 2
student_1['faculty'] = 'Philosophy'

# =============================================================================
# print(student_1)
# 
# del student_1['course']
# print(student_1)
# 
# # get metodi. Agar kalit so'z lug'atda bo'lmasa, ko'rsatilga boshqa qiymatni chiqarib beradi
# mevalar = {'olma':10000, 'tarvuz':8000, 'shaftoli':12000, 'qovun':11000}
# print(mevalar['olma'])
# 
# 
# meva = mevalar.get('uzum', 'Bunday meva mavjud emas')
# print(meva)
# 
# faculty = student_1.get('course')
# print(faculty)
# 
# meva_1 = mevalar.get('uzum')
# print(meva_1)
# =============================================================================

# =============================================================================
# print(student_0.items())
# 
# for key, value in student_0.items():
#     print(f"Key: {key}")
#     print(f"Value: {value} \n")
#     
# phones = {
#     'ali':'iphone 14 pro',
#     'vali':'samsung galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'nokia 3310'
#     }
# 
# for k, v in phones.items():
#     print(f"{k.title()}ning telefoni {v}")
# =============================================================================

mevalar = {'olma':10000, 
           'tarvuz':8000, 
           'shaftoli':12000, 
           'qovun':11000
           }

# =============================================================================
# print("Fruits in the market:")
# for fruit in mevalar.keys():
#     print(fruit.title())
#     
# bozorlik = ['anor', 'olma', 'baliq', 'qovun', 'non']
# for product in mevalar:
#     if product in bozorlik:
#         print(f"{product.title()} {mevalar[product]} so'm")
#         
# # Do'konda mahsulot bor yo'qligini aniqlash
# for buyum in bozorlik:
#     if buyum not in mevalar:
#         print(f"please, bring {buyum} to your market")
# =============================================================================
        
# =============================================================================
# for meva in sorted(mevalar):
#     print(meva.title())
# 
# print(mevalar.values())
# 
# =============================================================================

# =============================================================================
# phones = {
#     'ali':'iphone 14 pro',
#     'vali':'samsung galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'nokia 3310',
#     'amine':'iphone 14 pro',
#     'ahmed':'mi 10 pro',
#     'damian':'iphone 14 pro'
#     }
# for phone in phones.values():
#     print(phone)
#     
# print("\nPhones used by people")
# for phone in set(phones.values()):
#     print(phone)
# =============================================================================


# Sets Setning ichidagi elementlari output qilinganda takrorlanmaydi

toys = {'bear', 'car', 'horse', 'car', 'lamp', 'car', 'bear'}
print(toys)