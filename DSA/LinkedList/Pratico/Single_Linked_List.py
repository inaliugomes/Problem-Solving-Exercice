class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_all(self):
        if self.head == None:
            print("Lista vazia")
        else:
            temp = self.head
            while temp is not None:
                print(temp.data)
                temp = temp.next

    def add_begin(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
