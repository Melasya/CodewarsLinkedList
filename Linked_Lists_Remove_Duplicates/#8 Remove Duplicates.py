class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    if head is None:
        return None
    probe = head
    while probe is not None and probe.next is not None:
        if probe.data == probe.next.data:
            probe.next = probe.next.next
        else:
            probe = probe.next
    return head
