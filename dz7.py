###
# Число 179 записали 50 раз подряд.
# Полученное 150-значное число возвели в квадрат.
# Сколько получилось?
###
string = '179'*150
n = int(string)
res = n**2
print(res)


###
# n школьников делят k яблок поровну, неделящийся остаток остается в корзинке.
# Сколько яблок достанется каждому школьнику?
###

n = 3
k = 14
res = 14//3
print(res)


###
# Даны три целых числа. Определите, сколько среди них совпадающих.
# Программа должна вывести одно из чисел: 3 (если все совпадают),
# 2 (если два совпадает) или 0 (если все числа различны).
###
num1 = 2
num2 = 3
num3 = 3
if num1 == num2 and num1 == num3:
    res = 3
elif num1 == num2 or num1 == num3 or num2 == num3:
    res = 2
else:
    res = 0
print(res)


###
# Денис Павлович задал школьникам задачу:
# “Если данное четырехзначное число является симметричным, выведите 1,
# иначе выведите любое другое целое число”.
# Для проверки Денис Павлович использует заранее подготовленный набор тестов и правильных ответов к ним.
# Ире кажется, что она решила эту задачу, но тестирующая система Ejudge почему-то не принимает ее решение.
# Ира думает, что это происходит оттого, что она выводит не то любое другое число,
# которое записано в ответах у Дениса Павловича.
# Напишите программу, которая по ответу Дениса Павловича и по ответу Иры определяет,
# верно ли Ира решила задачу.
###
num = 1441
answ = 1
half1 = str(num)[:2]
half2 = str(num)[:1:-1]
if half1 == half2 and answ == 1:
    res = 'YES'
else:
    res = 'NO'
print(res)



###
# Дана строка. Если в этой строке буква f встречается только один раз, выведите её индекс.
# Если она встречается два и более раз, выведите индекс её первого и последнего появления.
# Если буква f в данной строке не встречается, ничего не выводите.
###
string = 'office'
f1 = string.find('f')
f2 = string.rfind('f')
if f1 == f2 and f1 != -1:
    print(f1)
elif f1 != f2 and f1 != -1:
    print(str(f1)+' '+str(f2))


###
# Дана строка, в которой буква h встречается минимум два раза.
# Удалите из этой строки первое и последнее вхождение буквы h,
# а также все символы, находящиеся между ними.
string = 'In the hole in the ground there lived a hobbit'
h1 = string.find('h')
h2 = string.rfind('h')
string = string.replace(string[h1:h2+1],'')
print(string)


###
# Дан текст в котором встречаются имена и следующие за ними фамилии.
# Нужно получить список фамилий (last name) людей которых зовут Иван. Если на английском, то Michael)
###

import re
text = "Michael, how are you? - Cool, how is John Williamns and Michael Jordan? I don\'t know but Michael" \
       " Johnson is fine. Michael do you still score points with LeBron James, Michael Green AKA Star and Michael Wood?"
res = re.findall(r'Michael \b[A-Z]\w+\b',text)
for names in res:
    last_names = names.split(' ')[1]
    print(last_names)
#print(res)