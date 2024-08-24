# arr=[1,4, 56, 78, 90 ]
#
#
#
#
# def binary_search(arr,tar):
#     low,high=0,len(arr)-1
#     while low<=high:
#         mid=(low+high)//2
#         if arr[mid]==tar:
#             return mid
#         elif arr[mid]>tar:
#             high=mid-1
#         else:
#             low=mid+1
#     return -1



# Class Stack
# append
# pop
#  list
from typing import Any

# Stack => push , pop , peek , is_empty,size
# class Stack:
#     def __init__(self):
#         self.stack = []
#
#     def is_empty(self) -> bool:
#         return len(self.stack) == 0
#
#     def push(self, item: Any) -> None:
#         self.stack.append(item)
#
#     def pop(self):
#         if not self.is_empty():
#             self.stack.pop()
#             return
#         raise Exception('Stack is empty')
#
#     def peek(self) -> Any:
#         if not self.is_empty():
#             return self.stack[-1]
#         raise Exception('Stack is empty')
#
#     def size(self) -> int:
#         return len(self.stack)
#
#
# stack = Stack()
# stack.push('john')
# stack.push('anna')
# stack.push('mike')
# stack.pop()
# stack.pop()
# stack.pop()
# stack.pop()
# print(stack.is_empty())


from collections import deque


# arr = deque()

# arr.appendleft(10)
# arr.appendleft(20)
# arr.appendleft(30)
# print(arr)
# Queue => dequeue , enqueue

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.appendleft(item)

    def dequeue(self):
        if not self.is_empty():
            self.queue.popleft()
            return
        raise Exception('Stack is empty')

    def is_empty(self):
        return len(self.queue) == 0

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        raise Exception('Stack is empty')

    def size(self):
        return len(self.queue)


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.dequeue()
queue.dequeue()
print(0)

# Linked List


# Node => data , next

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


    def delete_ldata(self,prev_data):
        if prev_data is None:
            raise Exception('The previous node is empty')


node1 = Node('dushanba')
node2 = Node('seshanba')
node3 = Node('chorshanba')

llist = LinkedList()
llist.head = node1
node1.next = node2
node2.next = node3
# llist.add_first_node('Yakshanba')
llist.last_add_node('payshanba')
llist.last_add_node('shanba')
llist.insert_node(node3.next, 'juma')
llist.show_all_nodes()
# llist.head.next = node2
# llist.head.next.next = node3
