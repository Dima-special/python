print("z x y w")
for z in range(2):
    for x in range(2):
        for y in range(2):
            for w in range(2):
                if (x and (z >= w) and not(y)) == 1:
                    print(z,x,y,w)