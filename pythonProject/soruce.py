# class Person:
#
#     def __init__(self, name="Babayka"):
#         self.name = name
#
#     def display_info(self):
#         print("My name is", self.name)
#
#     def __del__(self):
#         print("Я сдох")
#
#
# from OOP import Time
#
# val = Time(minutes=30, hours=4)
# val.find_time()
# from OOP import Price_product
#
# val1 = Price_product(price=120, count=5)
# val1.cost_product()
#
# from OOP import Motion
#
# val3 = Motion(speed=15, time_mine=3)
# val3.runaway()
#
# from OOP import Math
#
# val4 = Math(radius=3, height=3)
# val4.cone_volume()
# from OOP import Pifagor
#
# val5 = Pifagor(katet1=4, katet2=3)
# print(val5.area())
# from OOP import Gipotenuza
#
# val5 = Gipotenuza(katet1=4, katet2=3)
# print(val5.lenght())

#
# from main3 import Fraction

# val1 = Fraction(numerator=6, denominator=12)
# val2 = Fraction(numerator=2, denominator=3)
# val3= val1
# print(pow(val,3))
# print(pow(val,2)-pow(2,2))
# print(val1.reduction())

# from chernovik import Fraction


# def from_float_to_frac(in_float: float):
#     whole_part=int(in_float)
#     ost = in_float- int(in_float)
#     ten_nums = 10
#
#     while ost != 0:
#         whole_part *= 10
#         whole_part += ost * 10
#         ost *= 10
#         in_float = ost - int(ost)
#         ost //= 10
#         ten_nums *= 10
#
#     return Fraction(numerator=whole_part, denominator=ten_nums)
# a = Fraction(numerator=1, denominator=3)
# b = Fraction(numerator=2, denominator=5)
#
# c=2.9
# # print(a+b)
# print((c-int(c))//10)

# a = 113.333
#
#
# c= from_float_to_frac(a)
# print(c)

from chernovik import Fraction

c = Fraction(numerator=2, denominator=5)
print(c**0.5)
# c.from_float_to_frac(12.98)
# print(c)
