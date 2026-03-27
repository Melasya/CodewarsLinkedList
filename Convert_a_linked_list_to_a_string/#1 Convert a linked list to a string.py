class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def stringify(node):
    probe = node
    result = ""
    if node is None:
        return "None"
    while probe is not None:
        result += f"{(probe.data)}"
        probe = probe.next
        result += " -> "
    result += "None"
    return result

node = Node(1, Node(2, Node(3)))
print(stringify(node))
