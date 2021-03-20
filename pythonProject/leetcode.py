# class Solution:
#     def reverse(self, x: int) -> int:
#         if x<0:
#             x*=-1
#             y=str(x)
#
#             y*=-1
#         else:
#             y=str(x)
#             reversed(y)
#         if x >= -2 ** 31 or x <= (2 ** 31) - 1:
#             return 0
#         else:
#             return y
a=input('a=')
b = reversed(str(a))
x=int(b)
print(x)