def check(str):
    if len(list(str)) == len(set(str)):
        return "Дубликатов нет."
    else:
        return "Дубликаты есть."

print(check(input("Введите последовательность: ")))