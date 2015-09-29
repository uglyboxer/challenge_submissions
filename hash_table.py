class Item(object):

    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable(object):

    def __init__(self, size):
        self.size = size
        self.table = [[] for x in range(self.size)]

    def hash_function(self, key):
        return key % self.size

    def set(self, key, value):
        k = self.hash_function(key)
        self.item = Item(key, value)
        if self.table[k]:
            if self.table[k][0].key == key:
                self.table[k][0].value = value
            else:
                self.double_hash()
                k = self.hash_function(key)
                self.table[k].append(self.item)
        else:
            self.table[k].append(self.item)

    def get(self, key):
        k = self.hash_function(key)
        for i in self.table[k]:
            if i.key == key:
                return i.value
        else:
            return None

    def remove(self, key):
        k = self.hash_function(key)
        if self.table[k]:
            for idx, i in enumerate(self.table[k]):
                if i.key == key:
                    self.table[k].pop(idx)

    def double_hash(self):
        new_size = self.size * 2
        [self.table.append([]) for x in range(self.size + 1, new_size + 1)]
        self.size = new_size