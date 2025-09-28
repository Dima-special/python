print("z x w y")
for z in range(0,2):
    for x in range(0,2):
        for w in range(0,2):
            for y in range(0,2):
                if ((x == z) <= (not y or w)) != ((w <= z) or (x <= y)):
                    print(z, x, w, y)