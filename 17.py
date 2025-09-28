with open("C:\\Users\\Admin\\Desktop\\17-426.txt") as file:
    a = [int(i) for i in file.readlines()]
    
max_43 = max([i for i in a if i > 0 and abs(i)%100==43 and len(str(abs(i)))==5])

count = 0
m=-10000000000000000

for i in range(len(a)-2):
    l=[a[i],a[i+1],a[i+2]]
    b=(a[i])**2+(a[i+1])**2+(a[i+2])**2
    if len([i for i in l if abs(i)%100==43 and len(str(abs(i)))==5]) >= 1:
        if b <= max_43**2:
            count+=1
            m=max(m, b)
print(count,m)