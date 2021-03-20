# name = 'Joseph'
# def hello(a):
#     print((f'hello {name}'))
#
# hello(name)
# name = 'Joseph'
#
# def hello(a,*args):
#     print((f'hello {name}'))
#     for i in range(len(args)-1):
#         print()
# hello(name)
# a = 'a'
# print(ord(a))
# a = chr(122)
# print(a)
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
# s = 'The quick Brow Fox'
# x = 'Shohrux'
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
# print(search(x))

# word= 'madam'
# # def polindrom(s):
# for word in word:
#     if word == reversed(word):
#         print(word)
#     else:
#         print('no')
#
#
# # print(polindrom((s)))


text = "Anna"
text = text.lower()
a = text[::-1]


# def palindrome(txt, acopy):
#     for i in range(len(txt)):
#         if len(txt)-1 ==i:
#             pass
#         elif txt[i] == acopy[i]:
#             continue
#         elif txt[i] != acopy[i]:
#             return False
#         return True
#
#
# print(f'Palindrome is:{palindrome(text, a)} ')

# s = ('anna','madam','text')
# p=[]
# for s in s:
#     if s==s[::-1]:
#         p.append(s)
#
# print(p)
