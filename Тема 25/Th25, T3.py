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


class Queue:
    def __init__(self):
        self._front = None

    def push(self, item):
        node = Node(item)
        if not self._front:
            node.set_next(self._front)
            self._front = node
        else:
            current = self._front
            previous = None
            while current != None:
                previous = current
                current = current.get_next()
            previous.set_next(node)

    def pop(self):
        first_item = self._front.get_data()
        self._front = self._front.get_next()
        return first_item


q = Queue()
q.push(5)
q.push(4)
q.push(3)
print(q.pop())
print(q.pop())
