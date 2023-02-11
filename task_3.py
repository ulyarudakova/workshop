def func(num):
    x = [int(a) for a in str(num)]
    return(sum(x))

print(func(input("Введите целое число: ")))