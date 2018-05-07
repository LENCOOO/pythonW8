import numpy as np

a = int(input('请输入a:'))
b = int(input('请输入b:(b>a)'))
xi = float(input('请输入精度xi:'))
func=input("请输入函数：")
k = 0

def f(x):
    return eval(func)

while k == 0:
    if f(a) * f(b) > 0:
        pass
    elif f(a) * f(b) == 0:
        if f(a) == 0:
            print(a)
            k = 1
        else:
            print(b)
            k = 1

    else:
        m = 0.5 * (a + b)

        if (b - a) < xi:
            print(m)
            k = 1
        else:
            if f(a) * f(m) > 0:
                a = m
            else:
                b = m