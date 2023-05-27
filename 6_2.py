import time

start = time.time()

def polindrom(str):
    if str == str[::-1]:
        return("Это полиндром.")
    else:
        return("Это не полиндром.")
print(polindrom(input('Введите строку: ')))

end = time.time()
time_delta = end - start

filename = f"time_{time.strftime('%H:%M:%S %d.%m.%Y')}.txt"

with open(filename, 'w') as f:
    f.write(f"Время выполнения операции: {time_delta} секунд")

print(f"Время выполнения операции: {time_delta} секунд")

