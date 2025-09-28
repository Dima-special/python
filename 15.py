for a in range(1,50):
    count = 0
    for x in range(10000):
        if(((x%a==0) and (x%24==0) and (x%16!=0)) <= (x%a!=0))==1:
            count += 1
    if count == 10000:
        print(a)