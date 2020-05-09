from sys import argv

word = """
Network:
{0:<10} {1:<10} {2:<10} {3:<10}
{0:<10b} {1:<10b} {2:<10b} {3:<10b}
"""
word2 = word.replace('Network','/24')

mass = ['255','255','255','0']
addr = (('.'.join(argv[1:])).split('/')[0]).split('.')
addr.pop()
addr.append('1')

print(addr)
l = [int(i) for i in addr]
m = [int(i) for i in mass]
print(word.format(*l))
print(word2.format(*m))
