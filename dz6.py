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
pingvin= ['   _~_     ', '  (o o)    ', ' /  V  \\   ', '/(  _  )\\  ', '  ^^ ^^    ']
n = 3
file = open('pingvins.txt', 'w')
for lines in pingvin:
    print(lines*n)
    file.write((lines*n)+'\n')

file.close()

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
file = open('snail.txt', 'w')
print(lst)
file.write(str(lst))
file.close()

#print('   _~_     '*n)
#print('  (o o)    '*n)
#print(' /  V  \\   '*n)
#print('/(  _  )\\  '*n)
#print('  ^^ ^^    '*n)
