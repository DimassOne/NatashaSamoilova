IP = '192.168.3.1'
ip = IP.split('.')
word = """
{0:<10} {1:<10} {2:<10} {3:<10}
{0:<10b} {1:<10b} {2:<10b} {3:<10b}
"""

print(word.format(int(ip[0]),int(ip[1]),int(ip[2]),int(ip[3])))
