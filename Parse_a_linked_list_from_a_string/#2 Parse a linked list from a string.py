class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def linked_list_from_string(list_repr: str) -> Node | None:

    head = None
    if list_repr == "None":
        return None
    splited = list_repr.split(" -> ")
    del splited[-1]
    for node in reversed(splited):
        node = int(node)
        head = Node(node, head)
    return head

list_repr = "1 -> 2 -> 3 -> None"
print(linked_list_from_string(list_repr))
