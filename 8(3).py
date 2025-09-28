from itertools import *

number = 0
for i in product('01234', repeat=6):
    if i[0] != '1' and i[0] != '0': 
        if i[-1] != '3' and i[-1] != '4':
            number += 1
            
print(number)