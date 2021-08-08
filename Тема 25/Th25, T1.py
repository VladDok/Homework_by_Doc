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

class UnorderedList:

    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self._head)
        self._head = temp

    def size(self):
        current = self._head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()

        return count

    def search(self, item):
        current = self._head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()

        return found

    def remove(self, item):
        current = self._head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous is None:
            self._head = current.get_next()
        else:
            previous.set_next(current.get_next())

    #append
    def append(self, item):
        add_item = Node(item)
        current = self._head
        previous = None

        while current != None:
            previous = current
            current = current.get_next()

        previous.set_next(add_item)

    #index
    def index(self, idx):
        current = self._head
        amount = UnorderedList.size(self)

        if idx < amount and amount + idx > 0:
            if idx > 0:
                for _ in range(idx):
                    current = current.get_next()
            else:
                for _ in range(amount + idx):
                    current = current.get_next()

            return current.get_data()
        else:
            raise IndexError()

    #pop
    def pop(self, idx=-1):
        current = self._head
        previous = None
        amount = UnorderedList.size(self)

        if idx < amount and amount + idx > 0:
            if idx > 0:
                for _ in range(idx):
                    previous = current
                    current = current.get_next()
            else:
                for _ in range(amount + idx):
                    previous = current
                    current = current.get_next()

            previous.set_next(current.get_next())
        else:
            raise IndexError()

    #insert
    def insert(self, idx, item):
        new_data = Node(item)
        current = self._head
        previous = None
        amount = UnorderedList.size(self)

        if idx < amount and amount + idx > 0:
            if idx > 0:
                for _ in range(idx):
                    previous = current
                    current = current.get_next()
            else:
                for _ in range(amount + idx):
                    previous = current
                    current = current.get_next()

            new_data.set_next(current)
            previous.set_next(new_data)
        else:
            raise IndexError()

    #slice
    def slice(self, start, stop):
        current = self._head
        amount = UnorderedList.size(self)

        if start > stop:
            raise IndexError()

        if start < amount and amount + start > 0 and stop < amount and amount + stop > 0:
            if start > 0:
                for _ in range(start):
                    current = current.get_next()

                new_list = []

                for _ in range(start, stop):
                    new_list.append(current.get_data())
                    current = current.get_next()

                new_list.reverse()
                temp = UnorderedList()

                for item in new_list:
                    temp.add(item)

            elif start < 0:
                for _ in range(amount + start):
                    current = current.get_next()

                new_list = []

                for _ in range(amount + start, amount + stop):
                    new_list.append(current.get_data())
                    current = current.get_next()

                new_list.reverse()
                temp = UnorderedList()

                for item in new_list:
                    temp.add(item)

            return temp
        else:
            raise IndexError()

    def __repr__(self):
        representation = "<UnorderedList: "
        current = self._head
        while current is not None:
            representation += f"{current.get_data()} "
            current = current.get_next()
        return representation + ">"

    def __str__(self):
        return self.__repr__()


if __name__ == "__main__":
    my_list = UnorderedList()

    my_list.add(31)
    my_list.add(77)
    my_list.add(17)
    my_list.add(93)
    my_list.add(26)
    my_list.add(54)

    my_list.append(12)

    print(my_list)
    print(my_list.index(-2))
    my_list.pop(-2)
    print(my_list)
    my_list.insert(1, 25)
    print(my_list)
    print('-' * 30)
    print(my_list.slice(-1, -1))

