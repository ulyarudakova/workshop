import time

start = time.time()

def polindrom(str):
    if str == str[::-1]:
        return("Это полиндром.")
    else:
        return("Это не полиндром.")
print(polindrom(input('Введите строку: ')))

end = time.time()

print(int(end-start))
a = str(int(end-start))
print(time.strftime('%H:%M:%S %d.%m.%Y'))
b = str(time.strftime('%H:%M:%S %d.%m.%Y'))
with open("time.txt", 'w') as f:
    f.write(a)
    f.write("\n")
    f.write(b)

