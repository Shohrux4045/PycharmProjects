# 1
# tpl = (1, 2, 3, 4, 5)
# print(tpl)

# 2
# tpl = (1, 2, 3, ['hello', 'world'], [10, 23, 45])
# print(tpl)
#
# 3
# tpl = (1, 2, 3, ['hello', 'world'], [10, 23, 45])
# tpl1 = (1,)
# print(tpl1)
#
# 4
# tpl = (1, 2, 3)
# x = tpl[0]
# y = tpl[1]
# z = tpl[2]
# print(x, y, z)
#
# 5
# tpl = tpl = (1, 2, 3, ['hello', 'world'], [10, 23, 45])
# tpl[3].append('run')
# print(tpl)
#
# 7

# 6
# tpl = (1, 2, 3, ['hello', 'world'], [10, 23, 45])
#
# print(type(tpl))
#
# 8
# tpl = (2, 3, 4, [54, 23, 512], ['sara', 'siri'], 10, 11, 14)
# print(type(tpl[3]))
#
# 9
# tpl = (2, 3, 4, [54, 23, 512], ['sara', 'siri'], 10, 11, 14, 2, 3, 4)
# print(tpl.count(2))
#
# 10
# tpl = (1, 2, 3, ['hello', 'world'], [10, 23, 45])
# print(tpl.index('h')
#
# 11
# lst = [1, 2, 3, 4, 5]
# lst = tuple(lst)
# print(type(lst))
#
# 12
# tpl = (1, 2, 3, ['hello', 'world'], [10, 23, 45])
#13
# tpl = (2, 3, 4, [54, 23, 512], ['sara', 'siri'], 10, 11, 14)
# print(tpl[:2])
# 14
# tpl = (1, 2, 3, ['hello', 'world'], [10, 23, 45])
# print(tpl.index(2))
#
# 15
# tpl = (1, 2, 3, ['hello', 'world'], [10, 23, 45])
# print(len(tpl))
#17
# tpl = (1, 2, 3, ('hello', 'world'), (23, 45))
# for list in zip(tpl):
#     print(list, end='')

# 18
# a = (1, 2, 3, 10, 23)
# a = tuple(reversed(a))
# print(a)
#
# 20
# tpl = (100, 200, 300)
# print(f'это кортеж: {tpl}')
#
# 21
# tpl = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# tpl[0] = (10, 20, 100)
# tpl[1] = (40, 50, 100)
# tpl[2] = (70, 80, 100)
# print(tpl)
#
# # 22
# tpl = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
# tpl = [a for a in tpl if a != ()]
# print(tpl)
#
# tpl.remove(())
# tpl.remove(())
# print(tpl)
#
# 23
# tpl = [('item1', '12 .20 '), (' item2 ', '15 .10'), ('item3', '24 .5 ')]
a = tpl[0]
b = tpl[1]
c = tpl[2]

# 24
# не
# получился
# lst = [1, 2, 4, 5, 6, (20, 223, 45)]
# for a in lst:
#     if
# a != tuple:
# print(len(lst))
# break
#
# 25
# a = 'python 3.0'
# a = tuple(a)
# print(a)
#
# 26
# tpl1 = (4, 3, 2, 2, -1, 18)
# tpl2 = (2, 4, 8, 8, 3, 2, 9)
# print(f'умножение всех чисел указанного кортежа:{tpl1[0] * tpl1[1] * tpl1[2] * tpl1[3] * tpl1[4] * tpl1[5]}')
# print(f'умножение всех чисел указанного кортежа:{tpl2[0] * tpl2[1] * tpl2[2] * tpl2[3] * tpl2[4] * tpl2[5]}')
#
# 27
# tpl = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
# a = tpl[0]
# b = tpl[1]
# c = tpl[2]
# d = tpl[3]
#
# x = (a[0] + b[0] + c[0] + d[0]) / 4
# y = (a[1] + b[1] + c[1] + d[1]) / 4
# z = (a[2] + b[2] + c[2] + d[2]) / 4
# t = (a[3] + b[3] + c[3] + d[3]) / 4
# print((x, y, z, t))
#
# 28
# tpl = (('333', '33'), ('1416', '55'))
# a = tpl[0]
