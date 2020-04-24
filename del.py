word = 'Good morning, Good afternoon, Good evening'
ignore = ['morning','after','od']
number = word.find('morning')

for num in ignore:
    if word.find(num):
        print('Да строка входит')
    else:
        print ('Строки нет...')
