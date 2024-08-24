
# Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def show_all_nodes(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def add_first_node(self, new_data):
        node = Node(new_data)
        node.next = self.head
        self.head = node

    def last_add_node(self, new_data):
        node = Node(new_data)
        if self.head is None:
            self.head = node
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = node

    def insert_node(self, prev_node, new_data):
        if prev_node is None:
            raise Exception('The previous node is empty')
        node = Node(new_data)
        node.next = prev_node.next
        prev_node.next = node

    def delete_first_node(self):
        if self.head is None:
            raise Exception('The first node is empty')
        else:
            self.head = self.head.next

    def delete_any_node(self, node):
        if node.next is None:
            raise Exception('The node is empty')
        else:
            node.data = node.next.data
            node.next = node.next.next

    def delete_last_node(self):
        if self.head is None:
            raise Exception('The last node is empty')
        elif self.head.next is None:
            self.head = None
        else:
            node = self.head
            while node.next.next is not None:
                node = node.next
            node.next = None