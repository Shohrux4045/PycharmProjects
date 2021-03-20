# def pow_num(x, n):
#     if n == 0:
#         return 1
#     return x * pow_num(x, n - 1)
#
#
# print(pow_num(2, 2))

# def simpel_num(x, y=0):
#     y = x - 1
#     if x % y == 0:
#         print('ne prostoe')
#         return False
#     else:
#         return simpel_num(x, y-1 )
#
# print(simpel_num(7))
# a = 2
#
#
# def simple_number(a, number):
#     if number <= 1:
#         return False
#     elif a >= number:
#         print(number)
#     elif (number % a) == 0:
#         return False
#     else:
#         return simple_number(a + 1, number)
#     return True
#
#
# n = int(input("Enter : "))
# print(simple_number(a, n))


# def sum_of_list(lst):
#     sums = 0
#
#     for i in lst:
#         if isinstance(i, int):
#             sums += i
#         if isinstance(i, list):
#             sums += sum_of_list(i)
#
#     return sums
#
#
# l = [1, 2, 3, 4, [1], 5]
# print(sum_of_list(l))




