from sys import argv
script, files = argv
with open(files) as file:
    for i in file:
        print(i, end='')
