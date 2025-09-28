from ipaddress import *

for mask in range(33):
    net = ip_network('173.103.25.118/' +str(mask),0)
    print(net)