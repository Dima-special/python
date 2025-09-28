for a in range(1,50):
    count = True
    for x in range(10000):
        if(((x%a==0) and (x%24==0) and (x%16!=0)) <= (x%a!=0)) == 0:
            count = False
            break
    if count:
        print(a)