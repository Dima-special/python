from itertools import *

count = 0
for i in product('ДГИАШЕ', repeat=5):
    if i[0].count('А') == 0 and i[0].count('И') == 0 and i[0].count('Е') == 0 and i[4].count('Ш') == 0 and i[4].count('Г') == 0 and i[4].count('Д') == 0:
        count += 1

print(count)