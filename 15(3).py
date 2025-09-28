for a in range(1,200):
    count = 0
    for x in range(200):
        for y in range(200):
            if (x > 39) or (y > 26) or (2*x+ 4*y < a) == 1:
                count += 1
    if count == 200*200:
        print(a)