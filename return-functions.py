## Qiymat qaytaruvchi funksiyalar

### return orqali quyidagi funksiyadan qaytgan qiymatni biror bir (student1) o'zgaruvchiga saqlab qo'yiladi
# def make_fullname(name, surname):
#     """To'liq ism qaytaruvchi funksiya"""
#     fullname = f"{name.title()} {surname.title()}"
#     return fullname

# student1 = make_fullname("olim", "dolimov")
# student2 = make_fullname("ANVAR", "NARZULLAYEV")


# print(f"Darsga kelmagan o'quvchilar {student1} va {student2}")


def auto_info(company, model, colour, gearboxes, year, cost=None):
    auto = {
        'company': company,
        'model': model,
        'colour': colour,
        'gearboxes': gearboxes,
        'year': year,
        'cost': cost
    }

    return auto

auto1 = auto_info('GM', 'Malibu', 'Black', 'auto', 2022)
auto2 = auto_info('GM', 'Gentra', 'White', 'mechanic', 2021, 14000)
# # print(auto1)
# # print(auto2['cost'])

autos = [auto1, auto2]

print("We'll make a list of cars in our website.")
while True:
    print("\nEnter below info:")
    company = input("Producer of the car: ")
    model = input("Model of the car: ")
    colour = input("Colour of the car: ")
    gearboxes = input("Transmission of the car: ")
    year = input("Produced year: ")
    cost = input("Cost of the car: ")

    autos.append(auto_info(company, model, colour, gearboxes, year, cost))

    prompt = input("Will you add more cars? (yes/no)")
    if prompt == 'no':
        break


print("\n Cars in the Salon")
for auto in autos:
    if auto['cost']:
        cost = auto['cost']
    else:
        cost = "Undefined"
    print(f"{auto['colour'].title()} {auto['model'].title()}, {auto['gearboxes']} transmission. Cost: {auto['cost']}")

print(autos)

# print("Existing cars in the online market:")
# for auto in autos:
#     if auto['cost']:
#         cost = auto['cost']
#     else:
#         cost = "Undefinded"
#     print(f"{auto['colour']} {auto['model']}. Costs: {cost}")



#### Analog of range function
# def oraliq(min, max, step=1):
#     sonlar = []
#     if step == 1:
#         while min < max:
#             sonlar.append(min)
#             min += 1
#         return sonlar
#     else:
#         while min < max:
#             sonlar.append(min)
#             min = min + step
#         return sonlar

# numbs = oraliq(10, 20, 2)
# print(numbs)

# print(list(range(20,10,-2)))


