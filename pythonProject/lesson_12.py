# print("\n1 - Бить на байт " "\n2-байт на килобайт")
# a= input("Выбор:")
# if a == '1':
#     byt = (input('введите z = '))
#     kbyt= byt/1024
#
#     print(f'Перевод: {srt(b)}')

# import math
# def physics(R,L,C,):
#
#     return math.sqrt(R**2+(w*L-(1/w*C)))
# w=0.2
# r = float(input('введите R= '))
# l = float(input('введите L = '))
# c = float(input('введите C = '))
# print(physics(r,l,c))

# import pickle
#
# FILENAME = "user.dat"
#
# name = "Tom"
# age = 19
#
# with open(FILENAME,'wb') as file:
#     pickle.dump(name,file)
#     pickle.dump(age,file)
#
# with open(FILENAME,'rb') as file:
#     name = pickle.load(file)
#     age = pickle.load(file)
#     print("Имя: ", name,"\tВозраст: " ,age)

# import pickle
#
# FILENAME = "user.dat"
#
# user = [
#     ["Tom",28,True],
#     ["Alice",23,False],
#     ["Bob",34,False]
# ]
#
# with open(FILENAME,'wb') as file:
#     pickle.dump(user,file)
#
# with open(FILENAME,'rb') as file:
#     user_from_file = pickle.load(file)
#     for user in user_from_file:
#         print("Имя:", user[0], "\tВозраст: ", user[1],"\tЖенат(замужем) ",user[2])

# import shelve
# filename = "user"
#
# d = shelve.open(filename)
# d.close()
# import pickle
#
# import shelve
# FILENAME = "states2"

# with shelve.open(FILENAME) as states:
#     states["London"] = "Great Britian"
#     states["Paris"] = "Franc"
#     states["Berlin"]= "Germany"
#     states["Madrid"]= "Spain"
# with shelve.open(FILENAME) as states:
#     print(states["London"])
#     print(states["Paris"])
import shelve
#
# with shelve.open(FILENAME) as states:
#     for city in states.keys():
#         print(city,end=' ')
#     print()
#     for country in states.values():
#         print(country,end=' ')
# dict1= {
#     'users':[
#         {1:"qwerty.",2:"qwert2"},
#         {3:"qwerty3",4:"qwert4"}
#     ]
# }
# import shelve
# with shelve.open(students) as file:
#    file: [
#         {1: "qwerty", 2: "qwert2"},
#         {3: "qwerty3", 4: "qwert4"}
#     ]

    # file['student1'] = {' Шохрух': values1, '13-19': values2, 'Успеваемость:60'}
    # file['student1'] = {'Зокиров ': values1, '13-19': values2, 'Успеваемость:60'}
    # file['student1'] = {'Акбархон': values1, '13-19': values2, 'Успеваемость:100'}

# a = float(input('введите a= '))
# FILENAME = "states2"
# with shelve.open(FILENAME) as states:
#     states["a"] = a
# with shelve.open(FILENAME) as states:
#     h=((3**0.5)*a)/2
# with shelve.open(FILENAME) as states:
#     states.close()
# print(f'Высота: {h}')
R = float(input('введите R= '))
r = float(input('введите r= '))

FILENAME = "states2"
with shelve.open(FILENAME) as states:
    states["R"] = R
    states["r"] = r
    states["E"] = 285

with shelve.open(FILENAME) as states:
    I=states["E"]/(states["R"]+  states["r"] )
print(I)
