from itertools import * # product - с повторениями, permutations - без повторений

a=[]
number = 0
for i in product(sorted('ЛЕМУР'), repeat=4):
    number += 1
    if i[0] == 'Л':
        a.append(number)

print(min(a))
