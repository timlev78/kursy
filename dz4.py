#!/usr/bin/env python
# coding: utf-8

# In[2]:


###
# Напишите функцию min4(a, b, c, d), вычисляющую минимум четырех чисел, которая не содержит инструкции if, 
# а использует стандартную функцию min. Считайте четыре целых числа и выведите их минимум.
###

def min4(a, b, c, d):
    res = min(a, b, c, d)
    return res

num1 = 20
num2 = 9
num3 = -1
num4 = 200
print(min4(num1, num2, num3, num4))


# In[3]:


###
# Даны четыре действительных числа: x1, y1, x2, y2. 
# Напишите функцию distance(x1, y1, x2, y2), вычисляющую расстояние между точкой (x1,y1) и (x2,y2). 
# Считайте четыре действительных числа и выведите результат работы этой функции.
###

def distance(x1, y1, x2, y2):
    dist = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    return dist
x1 = 0
y1 = 0
x2 = 1
y2 = 1
print(distance(x1, y1, x2, y2))


# In[4]:


### 
# Проверьте, принадлежит ли точка данной закрашенной области: y=-x; y=2x+2; x^2+y^2 = 4 в точке (-1;1)
# Если точка принадлежит области (область включает границы), выведите слово YES, иначе выведите слово NO.
# Решение должно содержать функцию IsPointInArea(x, y), 
# возвращающую True, если точка принадлежит области и False, если не принадлежит. 
# Основная программа должна считать координаты точки, 
# вызвать функцию IsPointInArea и в зависимости от возвращенного значения вывести на экран необходимое сообщение.
# Функция IsPointInArea не должна содержать инструкцию if.
### 


# In[5]:


def IsPointInArea(x, y):
    return (y >=2*x+2)*(y>=-x)*((x+1)**2*(y-1)**2<=4)+(y<=2*x+2)*(y<=-x)*((x+1)**2*(y-1)**2>=4)

x = 4
y = -4
if IsPointInArea(x, y) == 1:
    print("yes")
else:
    print("no")


# In[11]:


###
# Создать консольную программу-калькулятор с интерактивным меню со следующими функциями:
# Сложение двух чисел
# Вычитание двух чисел
# Умножение двух чисел
# Деление двух чисел
# Возведение первого числа в степень второго числа
###
def summ(a, b):
    return (a + b)

def sub(a ,b):
    return (a - b)

def mul(a ,b):
    return (a * b)

def div(a ,b):
    if b == 0:
        print("Делить на ноль нельзя! \n")
        return 0
    else:
        return (a / b)
    
def st(a, b):
    return (a**b)

def Check(string, a, b):
    if ord(string) == 43:
        return summ(a, b)
    elif ord(string) == 45:
        return sub(a, b)
    elif ord(string) == 42:
        return mul(a, b)
    elif ord(string) == 47:
        return div(a, b)
    elif ord(string) == 94:
        return st(a, b)
    
while 1:
    a = int(input("Введите первое число: \n"))
    b = int(input("Введите второе число: \n"))
    act = input("Введите знак действия (+, -, *, /, ^): \n")
    print(str(a)+act+str(b)+'='+str(Check(act, a, b)))
    exit = input('Хотите выйти? (Y/N) \n')
    if exit == 'Y':
        break


# In[ ]:




