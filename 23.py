def f(x,n):
    if x == n: return 1 # 3 условия
    if x > n: return 0
    if x < n:
        return f(x+1,n) + f(x+2,n) + f(x*2,n) # ходы ну или операции 
    


print(f(4,11)*f(11,13)*f(13,52))