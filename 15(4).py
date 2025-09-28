for a in range(1,50):
    count = 0
    for x in range(200):
        for y in range(200):
            if ((5 < y) or (x > 32) or (x + 2*y < a)) == 1:
                count += 1
    if count == 200 * 200:
        print(a)