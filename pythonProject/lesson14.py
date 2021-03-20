# from math import cos, exp, atan, e, sqrt, fabs
#
#
# def fan(a, c, x):
#     L=(sqrt(exp(x) - cos(x ** 2 * a ** 5) ** 4) + atan(a - x ** 5) ** 4) / ((fabs(a + x * (c ** 4))) * (e / 2))
#     return L
#
# def main():
#     with open('math.txt','r') as file:
#         a = float(file.readline())
#         c = float(file.readline())
#         x = float(file.readline())
#
#     with open('math.txt', 'w') as file2:
#         L = str(fan(a, c, x))
#         file2.write(L)
#
#
# main()
# from math import sqrt ,sin ,cos
#
# def fan(x,c,t):
#     l=pow((cos(c)/sin(c)),2)+(2*pow(x,2)+5)/sqrt(c+t)
#     return l
#
# def main():
#     with open('math.txt','r') as file:
#         c = float(file.readline())
#         x = float(file.readline())
#         t = float(file.readline())
#
#     with open('out.txt', 'w') as file2:
#         l = str(fan(x,c,t))
#         file2.write(l)
#
#
# main()



# import math as m
#
# def fan(y,h):
#     a = (m.tan(pow(y, 3) + pow(h, 4)) + pow(h, 2)) / (m.sin(h) ** 3 + y)
#     return a
#
# def main():
#     with open('math.txt','r') as file:
#         y = float(file.readline())
#         h = float(file.readline())
#
#
#     with open('out.txt', 'w') as file2:
#         l = str(fan(y,h))
#         file2.write(l)
# main()
import math as m

def fun(y,x):
    f=(m.sqrt(pow(2+y,2)+(m.sin(y+5))*(1/7)))/(m.log(x+1)-pow(y,3))
    return f

def main():
    with open('math.txt','r') as file:
        y = float(file.readline())
        x = float(file.readline())


    with open('out.txt', 'w') as file2:
        a = str(fun(y,x))
        file2.write(a)
main()

