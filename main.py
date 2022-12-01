from calc.operations import Check
#import calc.history

while 1:
    a = int(input("Введите первое число: \n"))
    b = int(input("Введите второе число: \n"))
    act = input("Введите знак действия (+, -, *, /, ^): \n")
    print(str(a) + act + str(b) + '=' + str(Check(act, a, b)))
    exit = input('Хотите выйти? (Y/N) \n')
    if exit == 'Y':
        break