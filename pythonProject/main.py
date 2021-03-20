# def shohrux(n: int):
#     c = 0
#     if n > 1:
#         c = sum(range(1, n + 1))
#     elif n < 1:
#         c = sum(range(n, 2))
#
#     return c
#
#
# def timur(list_in: list):
#     set_d = set(list_in)
#     list_out = []
#     for i in set_d:
#         tmp = list_in.count(i)
#         list_out.append(tmp)
#         list_out.append(i)
#     return list_out
#
#
# def amal(n: int, k: int):
#     n *= 2
#     minutes = n // k
#     if n % k > 0:
#         minutes += 1
#     return minutes

# import packeg.fayl
# print(packeg.fayl.shohrux(n=2))