class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def isEmpty(self):
        if self.stack == []:
            return True
        else:
            return False


def genReverseString(string):
    generator = Stack()
    list_of_reverse_char = []

    for char in string:
        generator.push(char)

    while not generator.isEmpty():
        list_of_reverse_char.append(generator.pop())

    reversed_string = ''.join(list_of_reverse_char)
    return reversed_string


print(genReverseString('honey'))
print(genReverseString('unconscious'))
print(genReverseString('appear'))

