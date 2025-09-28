from itertools import *

odd = '1357'
even = '0246'

number = 0
for i in permutations('01234567', 5): # Если permutations, то 'repeat=' не пишется
    s = ''.join(i)
    if s.count ('1') == 0 and s[0] != '0':
        for i in range(len(s)-1):
            if s([i] in even and s[i+1] in even) or (s[i] in odd and s[i+1] in odd):
                break
        else:
            number += 1

print(number)