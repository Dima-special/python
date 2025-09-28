from math import *
def f(x,n):
    if x == n: return 1
    if x < n or (x == 26 or x == 30): return 0
    if x > n:
        return f(x-3,n) + f(int(x/2+0.5),n)
    
print(f(69,14))