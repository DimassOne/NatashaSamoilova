with open('sh_ip_interface.txt') as f:
    for line in f:
        if 'line protocol' in line:
            lin = line.split()[0]
        if 'MTU is' in line:
            lins = line.split()[-2]
            print('{:18}{}'.format(lin,lins))
