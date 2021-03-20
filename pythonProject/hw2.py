## 1
# for i in range(1500,2700):
#     if i%7 == 0 and i%5 == 0:
#         print(i)
# 2
# print('\n1 - Перевод градусов Фаренгейта (°F) в градусы Цельсия (°C)' '\n2 - Перевод градусов Цельсия (°C) градусы вФаренгейта (°F)' )
# a= int(input(' перевод: '))
# if a == 1:
#     f=int(input('Введите число °F:'))
#     c=(f-32)/1.8
#     print(c)
# elif a==2:
#     c = int(input('Введите число °C:'))
#     f=(c*1.8+32)
#     print(f)
# 3
# for i in range(1,10):
#     print(i)
# 6
# n = (1,2,3,4,5,6,7,8,9)
# even=odd=0
# for i in n:
#     if i % 2 == 0:
#             even += 1
#     else:
#         odd += 1
# print("четных -%i , нечетных -%i" % (even, odd))

# 7
# datalist = [1452, 11.23, 1 + 2j, True, 'w3resource', (0, -1), [5, 12], {"class": 'V', "section": 'A'} ]
# for a in datalist:
#     if a == datalist[int(input('index: '))]:
#         continue
#     print(type(a))
# 8
# for i in range(0,7):
#     if i==3 or i == 6:
#         continue
#     print(i,end=' ')
# 9
# f1 = f2 = 1
# n = int(input('n= '))
# for i in range(2,n):
#     f1, f2 = f2, f1 + f2
#     print(f1, end=' ')
# print()

# 10
# for i in range(0, 51):
#     if i % 3 == 0:
#         print("fizz")
#     elif i % 5 == 0:
#         print("buzz")
# print(i)
# for x in range(0, 51):
#     if x % 3 == 0 and x % 5 == 0:
#         print("FizzBuzz")
#     elif x % 3 == 0:
#         print("Fizz")
#     elif x % 5 == 0:
#         print("Buzz")
#     else:
#         print(x)
# 11
# 12
# a = input('Введите слово: ')
# print(a.lower())
# 14
# a=input('Слово: ')
# b=int(input("число: "))
# print(len(a),len(str(b)))
# 16
# for i in range(100,401):
#     if i%2 == 0:
#         print(i,end= ' ')
# 17
# result_str="";
# for row in range(0,7):
#     for column in range(0,7):
#         if (((column == 1 or column == 5) and row != 0) or ((row == 0 or row == 3) and (column > 1 and column < 5))):
#             result_str=result_str+"*"
#         else:
#             result_str=result_str+" "
#     result_str=result_str+"\n"
# print(result_str);

# 21L
# result_str="";
# for row in range(0,7):
#     for column in range(0,7):
#         if (((column == 1 or column == 1) and row!=0) or ((row ==6 or row == 6) and (column > 1 and column < 6))):
#             result_str=result_str+"*"
#         else:
#             result_str=result_str+" "
#     result_str=result_str+"\n"
# print(result_str);

# 23
# result_str="";
# for row in range(0,7):
#     for column in range(0,7):
#         if (((column == 6 or column ==2) and row != 0) or ((row == 1 or row ==6) and (column > 3 and column < 5))):
#             result_str=result_str+"*"
#         else:
#             result_str=result_str+" "
#     result_str=result_str+"\n"
# print(result_str);
# 28U
# result_str="";
# for row in range(0,7):
#     for column in range(0,7):
#         if (((column == 1 or column == 5) and row != 0) or ((row == 6 or row == 6) and (column > 1 and column < 5))):
#             result_str=result_str+"*"
#         else:
#             result_str=result_str+" "
#     result_str=result_str+"\n"
# print(result_str);


# 31

a = int(input('Введите возраст собаки в человеческих годах: ' ))
if a <= 2:
   age = a*10.5
   print("Возраст собаки в собачьих годах "  + str(age))
elif  a>2:
    age1 = ((a - 2) * 10 + (a - 2) * 4)
print("Возраст собаки в собачьих годах - " + str(age1))



# 32
# , у, о, ы, и, э, я, ю, ё, е
# x = input('Введите букву алфавита: ')
# if x == 1:
#     print( str(x) + ' -гласныЙ звук')
# elif x== 'б, в, г, д, ж, з, й, к, л, м, н, п, р, с, т, ф, х, ц, ч, ш, щ':
#     print(str(x)+'- согласный звук' )
#  , в, г, д, ж, з, й, к, л, м, н, п, р, с, т, ф, х, ц, ч, ш, щ

# 33

# print('\n1-январь' '\n2-февраль ' '\n3-март ' '\n4-апрель' '\n5-май' '\n6-июнь' '\n7-июль' '\n8-август ' '\n9-Сентябрь' '\n10-октябрь' '\n11-ноябрь' '\n12-декабрь')
# a= int(input('Месяц: '))
# if a == 1:
#     print('Кол-во дней: 30/31')
# elif a==2:
#     print('Кол-во дней: 28/29')
# elif a==3:
#     print('Кол-во дней: 30/31')
# elif a == 4:
#     print('Кол-во дней: 30/31')
# elif a==5:
#     print('Кол-во дней: 30/31')
# elif a ==6:
#     print('Кол-во дней: 30/31')
# elif a==7:
#     print('Кол-во дней: 30/31')
# elif a==8:
#     print('Кол-во дней: 30/31')
# elif a==9:
#     print('Кол-во дней: 30/31')
# elif a == 10:
#     print('Кол-во дней: 30/31')
# elif a == 11:
#     print('Кол-во дней: 30/31')
# elif a == 12:
#     print('Кол-во дней: 30/31')
# 34
# a = int(input("a= "))
# b = int(input('b= '))
# if 15 <= a + b < 20:
#     print(a + b)
# elif a + b == 20:
#     print(20)
# else:
#     print('What?')
# 35
# a = input('Введите строку: ')
# print(a.isdigit())

# 36
# a = int(input('a= '))
# b = int(input('b= '))
# c = int(input('c= '))
# if a > b > c > 0 or b > a > c > 0 or c > b > a > 0:
#     print("Разносторонний треугольник ")
# elif a == b == c > 0:
#     print("Равносторонний треугольник ")
# elif a == b > 0 or b == c > 0 or a == c > 0:
#     print('Равнобедренный треугольник ')
# else:
#     print("Такого треугольника не существует")
#

#
# 40
# a = int(input('a= '))
# b = int(input('b= '))
# c = int(input('c= '))
# s=(a+b+c)/3
# print(s)
#
# 41
# a = int(input('Введите год:  '))
# b = int(input('Введите месяц: '))
# c = int(input('Введите день: '))
# if 1<=c<=30 and 1<=b<=12:
#     print(c+1,b,a)
# elif c==31:
#     print(1,b+1,c)
# else:
#     print('No')
# result_str="";

# 43
# n = int(input("Число: "))
# for i in range(1, 11):
#     print(f"{i} x {n} = {n * i}")
