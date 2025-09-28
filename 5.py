j=[]
for i in range(1,100):
    n = bin(i)[2:]
    sum_=n.count('1')
    if sum_ %2 == 0:
        n = '10' + n
    else:
        n = '1' + n + '01'
    h = int(n,2)
    if h >516:
        j.append(i)
print(min(j))