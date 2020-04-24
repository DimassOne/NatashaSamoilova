ignore = ['duplex', 'alias', 'Current configuration']
with open('config_sw1.txt') as file:
    #Создаем и открываем для дозаписи новый файл duplicate.txt
    with open('duplicate.txt','w') as duplic:
        for line in file:
            duplic.write(line)
count = -1
with open('config_sw1.txt') as file:
    for line in file:
        for mas in ignore:
            if line.find(mas) >= 0:
                count +=1
        if count == -1:
            print(line, end='')
            count = -1
        else:
            count = -1

  
        

