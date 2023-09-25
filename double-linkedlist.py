class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """
        Purpose:
          this function adds node to linked list
        Parameters:
          data (int): int data
        Return:
          None
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        new_node.prev = last_node

    def prepend(self, data):
        """
        Purpose:
          this function adds node as a linked list's first item
        Parameters:
          data (int): int data
        Return:
          None
        """
        new_node = Node(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    def display(self):
        """
        Purpose:
          this function displays all linked list's data
        Parameters:
          None
        Return:
          None
        """
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def display_reverse(self):
        """
        Purpose:
          this function displays all linked list's data as reverse order
        Parameters:
          None
        Return:
          None
        """
        current = self.head
        while current and current.next:
            current = current.next
        while current:
            print(current.data, end=" ")
            current = current.prev
        print()



linked_list = DoublyLinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.prepend(0)
linked_list.display()  
linked_list.display_reverse()
