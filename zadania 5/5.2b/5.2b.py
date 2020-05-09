from slovar import london_co

slov = input("Введите пожалуйста r1, r2 или r3: ")
par = input("Введите параметр устройства (ios,model,vendor,location,ip): ")

print(london_co[slov][par])
