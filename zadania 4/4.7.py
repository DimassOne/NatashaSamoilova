MAC = 'AAAA:BBBB:CCCC'
mac = MAC.split(':')
print("{:b} {:b} {:b}".format(hex(mac[0]),hex(mac[1]),hex(mac[2])))
