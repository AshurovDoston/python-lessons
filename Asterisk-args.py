# ## *args
# def summa(*numbers):
#     """The function that calculates the sum of numbers"""
#     sum = 0
#     for numb in numbers:
#         sum += numb
#     return sum

# # print(summa(1,2,3,4))
# # print(summa(4,5,6,7,8,9,10,11,12,13))

# def summa2(x,y,*numbers):
#     return x+y+sum(numbers)

# print(summa2(1,2,3,4))


## **kwargs  =  keyword arguments
def auto_info(company, model, **infos):
    infos['kompaniya'] = company
    infos['modeli'] = model
    return infos

auto1 = auto_info("GM", "malibu", colour = 'black', year = 2020)
auto2 = auto_info("KIA", "k5", colour = 'silver', year = 2022, cost = 40000, type = 'sedan')
print(auto1)
print(auto2)