import time
import sys

while True:
    a = int(input('Введите число: '))
    if a > 0:
        time.sleep(a)
        print(input('Введите число: '))
    else:
        sys.exit()
