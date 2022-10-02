import modules as mod

auto = mod.auto_info("GM", 'malibu', 'black', 'auto transmission', 2022, 40000)
mod.info_print(auto)

#####
# when we use from (below) we don't need to mention the module name. Cause it imports function to our main file
print("\nBelow, case with FROM")
from modules import auto_info, info_print
auto = auto_info("GM", 'malibu', 'black', 'auto transmission', 2022, 40000)
info_print(auto)


######
# We can also change the function name when importing
print("\nBelow, case with changing function name")
from modules import auto_info as ainfo, info_print as iprint
auto = ainfo("GM", 'malibu', 'black', 'auto transmission', 2022, 40000)
iprint(auto)


########
# importing all functions. This is not recommeded
from modules import *


import math
x = 400
print(math.sqrt(x))
print(math.pow(5,4))
print(math.pi)
print(math.log10(100))

import random as r

number = r.randint(0,100)
print(number)

names = ['olim', 'zokir', 'akmal', 'nodir', 'sobir']
name = r.choice(names)
print(name.title())
print(r.choice(name))

x = list(range(15))
print(x)
r.shuffle(x)
print(x)