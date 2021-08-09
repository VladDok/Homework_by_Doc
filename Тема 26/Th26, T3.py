class HashTable:
    """Клас для створення хеш-таблиці."""
    
    def __init__(self, size):
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def hashing(self, key, size):
        return (key) % size

    def rehash(self, oldhash, size):
        return (oldhash + 1) % size

    def put(self, key, data):
        hashvalue = self.hashing(key, len(self.slots))
        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        elif self.slots[hashvalue] == key:
                self.data[hashvalue] = data
        else:
            if type(self.slots[hashvalue]) is not list:
                nextslot = self.rehash(hashvalue, len(self.slots))
                last = nextslot
                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot, len(self.slots))
                    if nextslot == last:
                        list_for_slots = [None] * self.size
                        list_for_data = [None] * self.size
                        list_for_slots.append(self.slots[hashvalue])
                        list_for_data.append(self.data[hashvalue])
                        list_for_slots.append(key)
                        list_for_data.append(data)
                        self.slots[hashvalue] = list_for_slots
                        self.data[hashvalue] = list_for_data
                        break
                else:
                    if self.slots[nextslot] == None:
                        self.slots[nextslot] = key
                        self.data[nextslot] = data
                    elif self.slots[nextslot] == key:
                        self.data[nextslot] = data

            else:
                self.slots[hashvalue].append(key)
                self.data[hashvalue].append(data)

    def get(self, key):
        startslot = self.hashing(key, len(self.slots))
        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            elif type(self.slots[position]) is list:
                idx = 0
                for item in self.slots[position]:
                    if item == key:
                        data = self.data[position][idx]
                        found = True
                    idx += 1
                else:
                    stop = True
            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

    def __contains__(self, searched_data):
        found = False
        for data in self.data:
            if type(data) is list:
                for item in data:
                    if item == searched_data:
                        found = True
            else:
                if data == searched_data:
                    found = True
        return found

    def __len__(self):
        count = 0
        for slot in self.slots:
            if type(slot) is list:
                for item in slot:
                    count += 1
            else:
                count += 1
        return count


table = HashTable(11)
table.put(1, 'cat')
table.put(4, 'dog')
table.put(55, 'frog')
table.put(32, 'fungus')
table.put(12, 'parrot')
table.put(567, 'cow')
table.put(123, 'big')
table.put(4567, 'berry')
table.put(234, 'duck')
table.put(122, 'funny')
table.put(1234, 'loli')
table.put(111, 'lucky')
table.put(12345, 'lolipop')
table.put(11111, 'asd')
table.put(3456, 'qwerty')
table.put(2, 'pop')
table.put(5, 'poli')
table.put(6, 'lol')
print(table.get(7))
print(table.get(12345))
print(table.get(2))
print(table[5])
print(len(table))
print('qwerty' in table)
print('fifa' in table)


                    
                
                
    

