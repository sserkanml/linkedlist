class Node:
    """
     Node class
    """

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """
    Linked list class
    """

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



linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.display()
