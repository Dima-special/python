print("z x w y")
for z in range(0,2):
    for x in range(0,2):
        for w in range(0,2):
            for y in range(0,2):
                if (((w <= y) <= x) or not(z))==0:
                    print(z, x, w, y)
#zywx