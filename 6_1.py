import time
import sys

a = int(input('Введите число: '))
print(a)
if a > 0:
    time.sleep(a)
    print(input('Введите число: '))
else:
    sys.exit()