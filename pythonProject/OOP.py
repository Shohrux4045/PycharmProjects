# class Person:
#     name = "Shohrux"
#
#     def display_info(self):
#         print("My name is", self.name)


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


# from soruce import Person
#
# val = Person(name="Shohrux")
# val.display_info()
# val = Person(name="Baxti")
# val.display_info()


# val.name = "Akbar"
# val.display_info()




# val1 = Person()
# val1.name = "Baxtiyor"
#

#
# val1.display_info()


class Time:

    def __init__(self, hours, minutes):
        self.minutes = minutes
        self.hours = hours

    def find_time(self):
        print("General minutes are", self.minutes + self.hours * 60)

    def __str__(self):
        return "Hours:"+str(self.hours)+",minutes:"+str(self.minutes)

    # def __add__(self, other):
    #     if isinstance(other,int):
    #         return Time(minutes=self.minutes+other, hours=self.hours)
    #     elif isinstance(other,Time):
    #         return Time(
    #             minutes=self.minutes+other.minutes,
    #             hours=self.hours+other.hours

        #     )
        # else:
        #     return None

    def __add__(self, other):
        if isinstance(other, int):
            return Time(minutes=self.minutes * other, hours=self.hours)
        elif isinstance(other, Time):
            return Time(
                minutes=self.minutes * other.minutes,
                hours=self.hours * other.hours

            )

    def right_format(self):
        if self.minutes >= 60:
            self.hours += self.minutes // 60
            self.minutes %= 60








#     def __del__(self):
#         pass
#         # print("Я сдох")
#
#
# class Price_product:
#
#     def __init__(self, price, count):
#         self.price = price
#         self.count = count
#
#     def cost_product(self):
#         print("total cost", self.price * self.count)
#
#     def __str__(self):
#         return
#     def __del__(self):
#         pass
#
#
# class Motion:
#
#     def __init__(self, speed, time_mine):
#         self.speed = speed
#         self.time_min = time_mine
#
#     def runaway(self):
#         print('distance traveled', self.speed * self.time_min * 60)
#
#     def __del__(self):
#         pass
#
#
# class Math:
#
#     def __init__(self, radius, height):
#         self.r = radius
#         self.h = height
#
#     def cone_volume(self):
#         v = (self.h * 2 * 3.14 * self.r) / 3
#         print(f"объем конуса-{v}")


# class Pifagor:
#
#     def __init__(self, katet1, katet2):
#         self.a = katet1
#         self.b = katet2
#
#     def area(self):
#         s = (self.a * self.b) / 2
#         return s


# class Gipotenuza:
#
#     def __init__(self, katet1, katet2):
#         self.a = katet1
#         self.b = katet2
#
#     def lenght(self):
#         c = (pow(self.a, 2) + pow(self.b, 2)) ** 0, 5
#         return c
#
# class Tangens:
#
#     def __init__(self,katet1,katet2):
#         self.a=katet1
#         self.b=katet2
#
#     def corner(self):
#         t=self.a/self.b
#         return t

