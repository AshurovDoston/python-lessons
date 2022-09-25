car_0 = {'model':'ferrari', 'colour':'red'}
print(car_0['model'])

mevalar = {'olma':10000, 'tarvuz':8000, 'shaftoli':12000, 'qovun':11000}
print(mevalar['olma'])
print(f"Tarvuz narxi {mevalar['tarvuz']} so'm")

student_0 = {
    'name':'murod olimov',
    'age':22,
    'birth_year':2022
    }

print(f"{student_0['name'].title()} \
      {student_0['birth_year']}-yilda tug'ilgan, \
    {student_0['age']} yoshda")

student_0['course'] = 4
student_0['faculty'] = 'Computer Science'
student_0['name'] = 'abdulloh'

# Empty dictionary
student_1 = {}
student_1['name'] = 'ismoil'
student_1['course'] = 2
student_1['faculty'] = 'Philosophy'

print(student_1)

del student_1['course']
print(student_1)

# get metodi. Agar kalit so'z lug'atda bo'lmasa, ko'rsatilga boshqa qiymatni chiqarib beradi
mevalar = {'olma':10000, 'tarvuz':8000, 'shaftoli':12000, 'qovun':11000}
print(mevalar['olma'])


meva = mevalar.get('uzum', 'Bunday meva mavjud emas')
print(meva)

faculty = student_1.get('course')
print(faculty)

meva_1 = mevalar.get('uzum')
print(meva_1)