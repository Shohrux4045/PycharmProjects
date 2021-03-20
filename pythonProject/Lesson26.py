import re
# a = input()

# gg = re.search(r'\d{3}\w{3}', a)
# if gg is not None:
#     print("Юр лицо")
#
# print(gg.group())

word = re.search((r'[а-яА-ЯёЁ]'), 'вас может возникнуть необходимость обозначить набор, в который входят буквы')

print(word.group())
# coding=utf-8


# re.match()
# re.search()
# re.findall()
# re.split()
# re.sub()
# re.compile()

# result = re.search(r'\d{4}-\d{2}-\d{2}', 'rfer 2021-03-17 Analytics Vidhya AV')
# print(result.start(), result.end(), result.group())
# r = result.group().split("-")
#
# for i, it in enumerate(r):
#     r[i] = int(it)
#
# print(r)

#
# def auto_num(string):
#     res = re.search(r'\w\d{3}\w{2}', string)
#     if res is not None:
#         print("Физ лицо")
#         return None
#     res = re.search(r'\d{3}\w{3}', string)
#     if res is not None:
#         print("Юр лицо")
#         return None
#     else:
#         print("Какая-та фигня!")
#         return None

result = re.findall(r'[0-9A-Za-z]{1,40}@\w{1,20}\.\w{1,20}', '4rtff433@wef.wef, малако,\nИм0л0коИхлеб')
print(result)

