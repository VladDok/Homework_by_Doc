class Node:
    def __init__(self, data):
        self._data = data
        self._next = None

    def get_data(self):
        return self._data

    def get_next(self):
        return self._next

    def set_data(self, data):
        self._data = data

    def set_next(self, new_next):
        self._next = new_next


class Stack:
    def __init__(self):
        self._head = None

    def push(self, item):
        node = Node(item)
        node.set_next(self._head)
        self._head = node

    def pop(self):
        last_item = self._head
        self._head = self._head.get_next()
        return last_item.get_data()

    def isEmpty(self):
        return self._head == None

    def peek(self):
        last_item = self._head
        return last_item.get_data()


s = Stack()
s.push(5)
s.push(4)
s.push(3)
print(s.pop())
print(s.peek())