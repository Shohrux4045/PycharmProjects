# 1
# def bigest(a, b, c):
#     if a > c and a > b:
#         print('bigest number=', a)
#     elif b > a and b > c:
#         print('bigest number=', b)
#     elif a == b:
#         print('a=b')
#     elif a == c:
#         print("a=c")
#     elif b == c:
#         print('b=c')
#     else:
#         print('bigest number=', c)
#
#
# bigest(4, 1, 1)

# # 2
# lst = (8, 2, 3, 0, 7)
#
#
# def sumlist(a, b, c, d, t):
#     return a + b + c + d + t
#
#
# print(sumlist(8, 2, 3, 0, 7))


# 3
# lst = (8, 2, 3, -1, 7)
#
#
# def sumlist(a, b, c, d, t):
#     return a * b * c * d * t
#
#
# print(sumlist(8, 2, 3, -1, 7))
# 4
# s = '1234abcd'
# def rever(s):
#     return reversed(s)
#
# print(rever(s))
# 5
# def fac(n):
#     if n == 0:
#         return 1
#     return fac(n-1) * n
#
#
# print(fac(10))

# 7
# s = 'The quick Brow Fox'
#
#
# def search(s):
#     a = 0
#     b = 0
#     for i in s:
#         if i <= chr(90) and i >= chr(65):
#             a += 1
#             # print(f'No.of Upper case characters:{i} ')
#         elif i >= chr(97) and i <= chr(122):
#             b += 1
#         # print(f'No.of lower case characters:{i} ')
#     return f'Upper: {a} lower: {b}'
#
#
# print(search(s))
#
# 8
# l = [1,2,3,3,3,3,4,5]
# def unity():
#     for i in l:


#  9
# def tub():
#     a =int(input("a= "))
#     if a%2==1 :
#         print('Это простое число')
#     else:
#         print('это сложное число')
#         return a
#
#
# tub()

# 10
# l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# def odd_search():
#     for i in l:
#         if i%2==0:
#             print(i,end=' ')
#
# odd_search()

# 11
# text = "Anna"
# text = text.lower()
# a = text[::-1]
#
#
# def palindrome(txt,acopy):
#     for i in range(len(txt)):
#         if len(txt)-1 == i:
#             return True
#         elif txt[i] == acopy[i]:
#             continue
#         elif txt[i] != acopy[i]:
#             return False
#         return True
#
#
# print(f'Palindrome is: {palindrome(text, a)}')

# 12


# 16
# def kv():
#     for i in range(1,31):
# import math

# print('Введите коэффициент уравнении')
#
# a = int(input('a= '))
# b = int(input('b= '))
# c = int(input('c= '))
#
# print("a*(x**2)+b*x+c = 0")
# D=b**2-4*a*c
# if D>0:
# 	x1 = float((-b+sqrt(D))/2*a)
# 	x2 = float((-b-sqrt(D))/2*a)
# 	print(f'корен квадрадного уравнения: ' ,{x1,x2})
# elif D<0:
# 	x = float(-b/2*a)
# 	print(f'корен квадрадного уравнения: ' ,{x})
# else:
# 	print('Без корня')
