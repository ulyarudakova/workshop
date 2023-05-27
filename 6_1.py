import time

while True:
    num = int(input("Введите число: "))
    if num < 0:
        break
    else:
        time.sleep(num)

print("Выход из программы")
