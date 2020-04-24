word = ['Protocol', 'Prefix','AD/Metric:','Next-Hop:','Last update:','Output Interfase:']
w = """{:<12} {:<12}
{:<12} {:<12}
{:<12} {:<12}
{:<12} {:<12}
{:<12} {:<12}
{:<12} {:<12}
"""
num = 0
with open('ospf.txt') as file:
    while True:
        num +=1
        text = file.readline().replace(',',' ').strip().split()
        print(w.format(word[0],text[0],
                       word[1],text[1],
                       word[2],text[2],
                       word[3],text[3],
                       word[4],text[4],
                       word[5],text[5]                   
                       ))
        if num == 7:
            break


