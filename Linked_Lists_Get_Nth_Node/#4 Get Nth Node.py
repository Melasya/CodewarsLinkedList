
# class Node(object):
#     """Node class for reference"""
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next
class Node:
    def __init__(self, data, next=None):
            self.data = data
            self.next = next

def get_nth(node, index):
    counter = 0
    if index < 0 :
        raise Exception("Index must be nonnegative")
    if node == None:
        raise Exception("There must be a list")

    while counter != index:
        node = node.next
        if node == None:
            raise Exception("The index is out of range")
        counter += 1

    return node
