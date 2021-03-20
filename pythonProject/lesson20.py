# a = None
#
# try:
#     a += 1
# except Exception:
#     a = 0
#
# print(a)
# from Fraction import Fraction
#
# a = Fraction(numerator=1, denominator=10.0)
# print(float(a))
#
#
# with open('registrations_.txt', 'r', encoding="utf-8") as file:
#     list_user = ''
#     list_of_user = file.readlines()
#     for user in list_of_user:
#         list_user += user
#
#     list = []
#     list.append(list_user.split('\n'))
#
#     print(list)
#
# with open("registrations_.txt", "r", encoding="utf-8") as file:
#     # output_file = open('text.txt', 'w')
#     list_user = ''
#     list_of_user = file.readlines()
#
#     for line in file:
#         g = line.splitlines(' ')
#
# print(g)
# list = []
# # # i = int(0)
# with open("registrations_.txt", "r", encoding="utf-8") as file:
#
#     for line in file:
#         tmp = line.split()
#         gg = tmp[0:]
#
#         print(gg[0])

# print(list)
# print(list[0][0])

# for i in range(1, 10):
#     gig = list[0][1]
# print(gig.isalpha())


#
# with open('registrations_.txt', 'r', encoding='utf-8') as file:
#     users_list = []
#     for line in file:
#         users = line.split()
#         users_list.append(users)
#
#
# # print(users_list)
# good_users_list = []
# bad_users_list = []
# i = 0
#
#
# for item in users_list:
#     a = item[:-2]
#     print(a)
# with open('registrations_.txt', 'r', encoding='utf-8') as file:
#     users_list = []
#     for line in file:
#         users = line.split()
#         users_list.append(users)
#
# # print(users_list)
# good_users_list_filter_full_elements = []
# good_users_list_filter_name = []
# good_users_list_filter_gmail = []
# bad_users_list = []
# item = 0
#
# for item in users_list:
#     if len(item) == 3:
#         good_users_list_filter_full_elements.append(item)
#     else:
#         bad_users_list.append(item)
#
# for item1 in good_users_list_filter_full_elements:
#     if item1[0].isalpha() and item1[2].isdigit():
#         good_users_list_filter_name.append(item1)
#     else:
#         bad_users_list.append(item1)
#
# for item2 in good_users_list_filter_gmail:
#     if "@" in item2[1] and "." in item2[1]:
#         good_users_list_filter_gmail.append(item2)
#     else:
#         bad_users_list.append(item2)
#
# print(bad_users_list)

# print(good_users_list_filter_full_elements)
list = ['1','2','skjdhgui']
# MyFile = open('text.txt', 'w')
# MyFile.writelines(list)
# MyFile.close()

list = ['1', '2', 'skjdhgui']
MyFile = open('text.txt', 'w')
for element in list:
    MyFile.write(element)
    MyFile.write(' ')


# with open('registration_good.log.txt', 'w',encoding='UTF-8') as good_users_list_filter_full_elements:
#     for line in  good_users_list_filter_full_elements:
#



#
# users_list = ['1', '2', '3']
#
# try:
#     for item in users_list:
#         if len(item) == 3:
#
# except ValueError:
