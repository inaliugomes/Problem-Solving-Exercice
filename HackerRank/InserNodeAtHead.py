class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

def insertNodeAtHead(llist, data):
    # Write your code here
    node = SinglyLinkedListNode(data)

    node.next = llist

    return node