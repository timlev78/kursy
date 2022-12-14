#!/usr/bin/env python
# coding: utf-8

# In[1]:


###
# Входные данные
# Вводятся 4 числа: a, b, c и d. 
#
# Выходные данные
# Выведите все числа на отрезке от a до b, дающие остаток c при делении на d. 
# Если таких чисел не существует, то ничего выводить не нужно.
###
a = 1
b = 10
c = 0
d = 2
for elem in range(a,b+1):
    if (elem % d) == c:
        print(elem)


# In[2]:


###
# По данному целому числу N распечатайте все квадраты натуральных чисел, не превосходящие N, в порядке возрастания.
###
N=100
for elem in range(int(N**0.5 + 1)):
    print(elem**2)


# In[3]:


###
# По данному числу N распечатайте все целые степени двойки, не превосходящие N, в порядке возрастания.
#
# Операцией возведения в степень пользоваться нельзя!
###

N=100
for elem in range(N+1):
    if pow(2,elem) <= N:
        print(pow(2,elem))


# In[4]:


###
# В первый день спортсмен пробежал x километров, а затем он каждый день увеличивал пробег на 10% от предыдущего значения. 
# По данному числу y определите номер дня, на который пробег спортсмена составит не менее y километров.
###

x = 10.0
y = 20.0
day = 1
while x < y:
    x += x * 0.1
    day += 1
print(day)


# In[7]:


### 
# По данному целому неотрицательному n вычислите значение n!.
###

n = 10
fact_n = 1
for elem in range(1,n+1):
    fact_n *= elem
print(fact_n)


# In[8]:


###
# Напишите программу, которая по данному числу n от 1 до 9 выводит на экран n пингвинов. 
# Изображение одного пингвина имеет размер 5×9 символов, 
# между двумя соседними пингвинами также имеется пустой (из пробелов) столбец. 
# Разрешается вывести пустой столбец после последнего пингвина. 
# Для упрощения рисования скопируйте пингвина из примера в среду разработки.
#   _~_    
#  (o o)   
# /  V  \  
#/(  _  )\ 
#  ^^ ^^   
###

n = 3
print('   _~_     '*n)
print('  (o o)    '*n)
print(' /  V  \\   '*n)
print('/(  _  )\\  '*n)
print('  ^^ ^^    '*n)


# In[35]:


###
# Очень топорная Улитка
###
n = 16
lst = [[1]]
size = int(n**0.5)
j = 0 #колонка
i = 0 #строка
for elem in range(2, n+1):
    if elem <= size:
        lst[0] += [elem]
#        print(lst)
        j += 1
    elif elem < size * 2:
        lst += [lst[0].copy()]
        i += 1
        lst[i][j] = elem
#        print(lst)
    elif (elem < size * 3) and (j > 0):
        j -= 1
#        print(j)
        lst[i][j] = elem
#        print(lst)
    elif (elem <= size * 3) and (j == 0):
        i -= 1
        lst[i][j] = elem
#        print(lst)
    elif (elem < size * size) and (j < size - 2):
        j += 1
        lst[i][j] = elem
#        print(lst)
    else:
        lst[i+1][j] = elem
        j -= 1
print(lst)


# In[ ]:




