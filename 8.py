from itertools import *

number = 0
for i in product(sorted('ПАРУС'), repeat=5):
    number += 1
    s = ''.join(i)
    if s.count ('У') <= 1 and ('АА') not in s:
        print(number)












