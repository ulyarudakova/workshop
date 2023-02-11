def season(i):
    if i in (12,1,2):
        return ("зима")
    elif i in (3,4,5):
        return ("весна")
    elif i in (6,7,8):
        return ("лето")
    elif i in (9,10,11):
        return("осень")

print(season(int(input("Введите номер месяца"))))