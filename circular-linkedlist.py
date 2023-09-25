class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
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
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

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
        if self.head:
            while True:
                print(current.data, end=" ")
                current = current.next
                if current == self.head:
                    break
        print()


linked_list = CircularLinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.display()
