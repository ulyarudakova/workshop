def polindrom(str):
    if str==str[::-1]:
        return("Это полиндром.")
    else:
        return("Это не полиндром.")

print(polindrom(input("Введите строку: ")))