import re

#
# def word_search(string):
#     word = re.search((r'[а-яА-ЯёЁ]'), 'вас может возникнуть необходимость обозначить набор, в который входят буквы',
#                      string)
#
#     print(word.group())


# def abbreviations():
abb = re.findall('r\w[А-Я],', 'Это курс информатики соответствует ФГОС и ПООП это подтверждено ФГУ ФНЦ НИИСИ РАН')

print(abb)

# import re
#
# word = re.findall("([A-Z]\.*){2,}s?", "hello, look an ACRONYM")
# print(word)
