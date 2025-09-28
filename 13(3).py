from ipaddress import *

for mask in range(33):
    net = ip_network('154.201.208.17/' +str(mask),0)
    print(net)

# 19
# 11111111.11111111.11100000.00000000  3 байт это '11100000', переводим в 10-ю это и ответ