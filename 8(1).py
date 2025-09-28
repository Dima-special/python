from itertools import *

count = 0
for i in product('01234', repeat=6): # в кавычках система счисления(здесь пятиричная), после repeat= такая цифра, какое число нам нужно(тут шестизначное)
    if i[0] != '0' and i[0] != '1':
        if i[-1] != '3' and i[-1] != '4':
            count += 1

print(count)