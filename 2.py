#С клавиатуры вводятся числа, пока не будет введён 0 (каждое число в новой строке).
#Требуется подсчитать сумму всех нечётных положительных чисел. Сами числа и сумму вывести на экран
e = input('Введите число: ')
list = []
summ = 0
while e != '0':
    if '.' not in e:
        e = int(e)
        if e % 2 != 0 and e > 0:
            list.append(e)
            summ += e
    else:
        e = float(e)
        if e % 2 != 0 and e > 0:
            list.append(e)
            summ += e
    e = input('Введите число: ')
print(list)
print(summ)
