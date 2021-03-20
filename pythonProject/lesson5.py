# for i in range(0,5):
#     for j in range(0,5):
#         print("*", end='')
#     print()
# for i in range(6):
#     for j in range(i):
#         print("*", end='')
#     print()

# for i in range(k):
#     for j in range(k):
#         if j<= i:
#          print("*", end='')
#     print()


#
# k=3
#
# for i in range(k):
#     for j in range(k):
#         if j== i:
#          print("*", end='')
#         else:
#             print(' ', end='')
#     print()
# lenght=len(range(k))-1
# for i in range(k):
#     for j in range(k):
#         if j == lenght:
#          print('*', end='')
#         else:
#             print(' ', end='')
#     lenght -=1
#     print()
# k=6
# first = ''
# first_list = []
# second = ''
# second_list = []
# total = []

# lenght=len(range(k))-1
# for i in range(k):
#     for j in range(k):
#         if j == lenght:
#             first += '*'
#         else:
#             first += ' '
#
#     first_list.append(first)
#     first = ' '
#     lenght -=1
#
#     print(first_list)

# for i in range(k):
#     for j in range(k):
#         if j== i:
#          second += '*'
#         else:
#             second =' '
#     print(second_list)
# i = 1
# while i <=10:
#     print(i, end=' ')
#     i+=1
# s = 'Hello world'
# for l in s:
#     if l == ' ':
#         continue
#     print(l, end=' ')
# for i in 'HelloWorld':
#     if i == ' ':
#         break
#     print(i, end=' ')
# else:
#     print('\nNO SPACE')
# i=1900
# while i<=2020:
#     print(i)
#     i+=1
# if 1:
#     print('Выражения  ИСТИННО')
# else:
#     print('Выражения  ЛОЖЬ')
# light = 'yellow'
#
# if light == 'red':
#     print('Stop')
# elif light == 'yellow':
#     print('Wait')
# elif light == 'green':
#     print('Go')
# else:
#     print('What?')

# age = int(input('Сколько вам лет?:'))
#
# if age >= 18:
#     print('Добро пожаловать')
# else:
#     print('Вам еще рано')
#
# t1 = tuple ('Hello')
# t2 = tuple('world')
# t3=t1 + t2
# # print(t3)
# # print(len(t3))
# # print(t3.count('l'))
# print(t3.index('o'))
# t1 = (10, 11, [1,2,3],[4,5,6],['hello', 'world'])
#
# t1[4][0] =  'new'
# t1[4].append('hello')
# print(t1, id(t1))
result_str="";
for row in range(0,7):
    for column in range(0,7):
        if (((column == 1 or column == 5) and row != 0) or ((row == 0 or row == 3) and (column > 1 and column < 5))):
            result_str=result_str+"*"
        else:
            result_str=result_str+" "
    result_str=result_str+"\n"
print(result_str);

