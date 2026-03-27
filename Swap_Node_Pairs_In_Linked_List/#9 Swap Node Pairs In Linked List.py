class Node:
    def __init__(self, next=None):
        self.next = next

def swap_pairs(head):
    prev = None
    current = head
    if head is None or head.next is None:
        return head
    swaped_head = head.next #B
    while current is not None and current.next is not None:
        second = current.next
        next_pair = current.next.next #C
        second.next = current #B -> A
        current.next = next_pair
        if prev is not None:
            prev.next = second
        prev = current
        current = current.next
    return swaped_head
