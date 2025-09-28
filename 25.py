from fnmatch import *

for i in range(0,10):
        for j in range(0,10):
            n= int(f'12345{i}6{j}')
            if n % 17 == 0:
                  print(n,n//17)