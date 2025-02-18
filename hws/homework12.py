from typing import List, Optional

class StaticArray:
    def __init__(self, capacity: int):
        self.array = [None] * capacity
        self.capacity = capacity

    def set(self, index: int, value: int) -> None:
        self.array[index] = value

    def get(self, index: int) -> int:
        return self.array[index]

class DynamicArray:
    def __init__(self):
        self.array = []

    def append(self, value: int) -> None:
        self.array.append(value)

    def insert(self, index: int, value: int) -> None:
        self.array.insert(index, value)

    def delete(self, index: int) -> None:
        self.array.pop(index)

    def get(self, index: int) -> int:
        return self.array[index]

class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value: int) -> None:
        if not self.head:
            self.head = Node(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(value)

    def insert(self, position: int, value: int) -> None:
        new_node = Node(value)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for _ in range(position - 1):
                if current is None:
                    return
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def delete(self, value: int) -> None:
        if self.head and self.head.value == value:
            self.head = self.head.next
            return
        current = self.head
        while current and current.next:
            if current.next.value == value:
                current.next = current.next.next
                return
            current = current.next

class DoubleNode:
    def __init__(self, value: int, next_node=None, prev_node=None):
        self.value = value
        self.next = next_node
        self.prev = prev_node

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value: int) -> None:
        new_node = DoubleNode(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value: int) -> None:
        self.queue.append(value)

    def dequeue(self) -> int:
        return self.queue.pop(0)

    def peek(self) -> int:
        return self.queue[0]

    def is_empty(self) -> bool:
        return len(self.queue) == 0

class TreeNode:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value: int) -> None:
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.value:
            if node.left:
                self._insert(node.left, value)
            else:
                node.left = TreeNode(value)
        else:
            if node.right:
                self._insert(node.right, value)
            else:
                node.right = TreeNode(value)

def insertion_sort(lst: List[int]) -> List[int]:
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst

def selection_sort(lst: List[int]) -> List[int]:
    for i in range(len(lst)):
        min_idx = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst

def bubble_sort(lst: List[int]) -> List[int]:
    n = len(lst)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst