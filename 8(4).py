from itertools import *


number = 0
for i in permutations('ИГРОК', 5): # Если permutations, то 'repeat=' не пишется
    s = ''.join(i)
    if s.count ('РОК') == 0 and s[0] != 'К':
        number += 1
print(number)