class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def sorted_insert(head, data):
    probe = head
    prev = None
    #probe стоїть на вузлі після місця вставки.
    #але нам треба змінити .next у вузла перед місцем вставки.
    #а ми його вже "проїхали" і не пам'ятаємо!
    #Тому prev просто йде на крок позаду probe:
    insert_node = Node(data) #це вузол який містить це число: Node(5), тобто об'єкт з .data і .next
    while probe is not None and data > probe.data:
        prev = probe #запам'ятовує поточний
        probe = probe.next #probe йде далі

    insert_node.next = probe #insert_node дивиться на решту списку
    if prev is None: #вставляємо на початок
        head = insert_node
    else: #вставляємо в середину або кінець
        prev.next = insert_node

    return head
