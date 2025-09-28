from fnmatch import *

for i in range(10**8):
    if fnmatch(str(i), '1234*7'):
        if i % 141 == 0:
            print(i, i//141)