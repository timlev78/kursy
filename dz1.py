#!/usr/bin/env python
# coding: utf-8

# In[3]:


num1 = int(input("Введите первое число: \n"))
num2 = int(input("Введите второе число: \n"))
num3 = int(input("Введите третье число: \n"))
num4 = int(input("Введите четвёртое число: \n"))
num5 = int(input("Введите пятое число: \n"))
if num1 < num2:
    min_num = num1
else:
    min_num = num2
if num3 < min_num:
    min_num = num3
if num4 < min_num:
    min_num = num4
if num5 < min_num:
    min_num = num5
print(f"Минимальное число: {min_num}")


# In[ ]:




