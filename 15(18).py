d = [i for i in range(17,59)]
c = list(range(29,81))
a = []

for x in range(1,100):
    if ((x in d) <= (((x not in c) and (x not in a)) <= (x not in d))) == 0:
        a.append(x)

print(a)
#смотрим по границам