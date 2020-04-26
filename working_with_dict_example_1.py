from pprint import pprint
result = dict()
with open('sh_ip_int_br.txt') as f:
    for line in f:
        line = line.split()
        print(line)
        if line and line[1][0].isdigit():
            print(line[1][5])
            interface, address, *other = line
            result[interface] = address

pprint(result)
