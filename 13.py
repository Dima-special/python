from ipaddress import *

net = ip_network('122.159.136.144/255.255.255.248',0) #1-ое - IP-адрес, 2-ое - маска подсети

for ip in net:
    b=f"{ip:b}"
    if b.count('1') %4 !=0:
        print(b)

