def f(a,b,m,): # Задание с 2-мя кучами a - кол-во камней 1-я куча, b - кол-во камней 2-я куча, m - это ходы
    if a + b >= 59: return m%2==0 # Условие победы a+b >= 59 (59 - это кол-во камней при котором будет выигрыш)
    if m == 0: return 0
    h = [f(a,b,m-1), f(a,b,m-1), f(a,b,m-1), f(a,b,m-1)] # h в данном случае - это типы ходов
    return any(h) if (m-1)%2==0 else any(h) # (any any), когда неудачная игра пети (в 19), а (в 20 и 21) при любой игре будет (any all)

print("19) ", [s for s in range(1,59) if f(5,s,2)])
print("19) ", [s for s in range(1,54) if f(5,s,2) and not f(5,)])
print("19) ", [s for s in range(1,54) if f(5,s,2)])