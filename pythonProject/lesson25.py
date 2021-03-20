import math


# lst = [1, 2, 5]
# mylist = [math.sqrt(x)*j for x in lst for j in range(5)]
# print(len(mylist))
#
#
# def all_perms(elements):
#     if len(elements) <= 1:
#         yield elements
#     else:
#         for perm in all_perms(elements[1:]):
#             for i in range(len(elements)):
#                 yield perm[:i] + elements[0:1] + perm[i:]
#
#
# for i in all_perms([1, 3, 7, 9]):
#     print(i)

#
# # Графы
#
# class Vertex:
#
#     def __init__(self, value, connection=None):
#         self.value = value
#         self.ribs = []
#         if connection is not None:
#             self.ribs.append(connection)
#
#     def add_connection(self, connection):
#         if isinstance(connection, Vertex):
#             self.ribs.append(connection)
#             # connection.add_connection(self)
#
#     def __str__(self):
#         return str(self.value) \
#                + ",with cout of connection " \
#                + str(len(self.ribs))
#
#
# a = Vertex(value=3)
# b = Vertex(value=4)
#
# a.add_connection(b)
# b.add_connection(a)
#
#
# print(b.ribs[0])


# class TreeVertex:
#
#     def __init__(self, value, right_child=None, left_child=None):
#         self.value = value
#         self.right_child = right_child
#         self.left_child = left_child
#
#     def sef_right_child(self, item):
#         if isinstance(item, TreeVertex):
#             self.right_child = item
#
#     def set_left_child(self, item):
#         if isinstance(item, TreeVertex):
#             self.left_child = item

def all_perms(elements):
    if len(elements) <= 1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:]


for i in all_perms([1, 3, 7, 9]):
    # if sum(i[:2]) == sum(i[2:]):
        print(i[2:])
        # print("True")

