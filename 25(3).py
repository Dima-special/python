from fnmatch import *

def s (n):
    sum_=0
    for digit in str(n):
        sum_ += int(digit)
    return sum_

for i in range(700_000, 700_244):
    if not fnmatch(str(i), '*0??3*') and not fnmatch(str(i), '*4??2') and not fnmatch(str(i), '*1*'):
        if i % 13 == 0:
            print(i, s(i))