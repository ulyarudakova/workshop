import time

today = time.time()
f = input('Введите дату своего рождения в формате дд.мм.гггг: ')
date = time.mktime(time.strptime(str(f), '%d.%m.%Y'))
print('Прожито дней: ', int((today - date)/86400))



