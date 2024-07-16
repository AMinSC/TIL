class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    def insert_after(self, prev_node, data):
        if prev_node is None:
            print("Previous node must be in LinkedList!")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        if new_node.next:
            new_node.next.prev = new_node

    def delete(self, node):
        if self.head is None or node is None:
            return
        if self.head == node:
            self.head = node.next
        if node.next:
            node.next.prev = node.prev
        if node.prev:
            node.prev.next = node.next

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")


if __name__ == "__main__":
    doubly_linked_list = DoublyLinkedList()
    doubly_linked_list.append(1)
    doubly_linked_list.append(2)
    doubly_linked_list.append(4)

    doubly_linked_list.print_list()

    doubly_linked_list.insert_after(doubly_linked_list.head.next, 3)
    doubly_linked_list.print_list()

    doubly_linked_list.delete(doubly_linked_list.head.next.next)
    doubly_linked_list.print_list()