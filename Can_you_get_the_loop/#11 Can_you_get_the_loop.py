def loop_size(node):
    slow = node
    fast = node
    #finding the meeting point inside the loop
    while True:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    #th elength of the cycle
    count = 1
    current = slow.next
    while current != slow:
        current = current.next
        count += 1
    return count
