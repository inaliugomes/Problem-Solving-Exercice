from DSA.LinkedList.Pratico.Node import Node


class SingleLinkedList:
    def __init__(self):
        self.tail = None
    def append(self,date):
        node = Node(date)
        #To search the next value we haved the need to iterate for all object in my linked list
        if self.tail is None:
            self.tail = node
        else:
            current = self.tail
            while current.next is not None:
                current = current.next
            current.next = node