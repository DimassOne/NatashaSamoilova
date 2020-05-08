command1 = 'switchport trunk allowed vlan 1,3,10,20,30,100'
command2 = 'switchport trunk allowed vlan 1,3,100,200,300'
com1 = set((command1.split(' ').pop()).split(','))
com2 = set((command2.split(' ').pop()).split(','))
print(com1.intersection(com2))
#Можно было сделать так:
print(set((command1.split(' ').pop()).split(',')).intersection(set((command2.split(' ').pop()).split(','))))
