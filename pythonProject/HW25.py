# class Terak():
#     def __init__(self, data):
#         self.data = data
#         self.children = []
#
#     def add_child(self, gg):
#         self.children.append(gg)
#
# a = Terak(1)
# b = Terak(2)
# c = Terak(3)
#
# a.add_child(b)
# a.add_child(c)
#
# for i in a.children:
#     print(i)

class TreeNode:
    def __init__(self, data, right=None, left=None):
        self.data = data
        self.right = right
        self.left = left

    def set_right_child(self, right_child):
        self.right = right_child

    def set_left_child(self, left_child):
        self.left = left_child

    def __str__(self):
        return str(self.data)


def go_around(tree: TreeNode):
    if tree.right is None and tree.left is None:
        print(tree.data)
        return None
    if tree.right is not None:
        go_around(tree.right)

    print(tree.data)

    if tree.left is not None:
        go_around(tree.left)


a = TreeNode(data=1)

a.right = TreeNode(data=3)
a.left = TreeNode(data=2)

a.left.right = TreeNode(data=6)
a.left.left = TreeNode(data=7)

a.right.right = TreeNode(data=4)
a.right.left = TreeNode(data=5)

a.left.right.left = TreeNode(data=8)
a.right.left.right = TreeNode(data=9)

go_around(a)
