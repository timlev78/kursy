from calc.history import log_write

def summ(a, b):
    return (a + b)


def sub(a, b):
    return (a - b)


def mul(a, b):
    return (a * b)


def div(a, b):
    if b == 0:
        print("Делить на ноль нельзя! \n")
        return 0
    else:
        return (a / b)


def st(a, b):
    return (a ** b)


def Check(string, a, b):
    if ord(string) == 43:
        res = summ(a, b)
    elif ord(string) == 45:
        res = sub(a, b)
    elif ord(string) == 42:
        res = mul(a, b)
    elif ord(string) == 47:
        res = div(a, b)
    elif ord(string) == 94:
        res = st(a, b)
    log_write(string, a, b, res)
    return res
