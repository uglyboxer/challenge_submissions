# Author: Cole Howard
#
# Creates a hash table and lookup/add system.  In cases of key collisions
# the size of the table is doubled and the hash key is dynamically updated


class Item(object):

    def __init__(self, key, value):
    """ Create an item with a key and value

    Args:
        key: an int 
        value: anything
    """
        self.key = key
        self.value = value


class HashTable(object):

    def __init__(self, size):
        """
        Args:
            size: an int
        """

        self.size = size
        self.table = [[] for x in range(self.size)]

    def hash_function(self, key):
        """ Args:
                key: an int 
        """
        return key % self.size

    def set(self, key, value):
        """ Sets a value in the table for a given key

        Args:
            key: an int 
            value: anything
        """
        k = self.hash_function(key)
        self.item = Item(key, value)
        if self.table[k]:                       # Check for hash presence
            if self.table[k][0].key == key:     # Check for specific presence
                self.table[k][0].value = value
            else:
                self.double_hash()              # Handle collision
                k = self.hash_function(key)
                self.table[k].append(self.item)
        else:                                   # Or just add it
            self.table[k].append(self.item)

    def get(self, key):
        """" Returns value for a given key

        Args:
            key: an int 
        """
        k = self.hash_function(key)
        for i in self.table[k]:
            if i.key == key:
                return i.value
        else:
            return None

    def remove(self, key):
        """ Removes an entry from the table

        Args:
            key: an int
        """
        k = self.hash_function(key)
        if self.table[k]:
            for idx, i in enumerate(self.table[k]):
                if i.key == key:
                    self.table[k].pop(idx)

    def double_hash(self):
        """ Doubles the table and "indirectly" alters the hash hash_function"""
        new_size = self.size * 2
        [self.table.append([]) for x in range(self.size + 1, new_size + 1)]
        self.size = new_size


if __name__ == '__main__':
    pass