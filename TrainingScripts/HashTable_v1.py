'''
Make a Hash Table module for other script to use
'''


class HashTable:
    def __init__(self):
        self.size = 256 # Default Hash table length
        self.slots = [None for i in range(self.size)] # Initial a empty hash table with none value
        self.count = 0
        self.key = "default"
        self.value = "default"

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def _hashitem(self, key, value):
        self.key = key
        self.value = value

    # Calculate a unique hash numeric for a input string & return a hash table index number
    def _hash(self, key):
        mult = 1
        hv = 0
        for ch in key:
            hv += mult * ord(ch)
            mult += 1
        return hv % self.size

    # A operation function for input data into hash table(linear solution for hash key conflict)
    def put(self, key, value):
        self._hashitem(key, value)
        h = self._hash(key)
        #print(h)
        while self.slots[h] is not None:
            if self.slots[h][0] is self.key:
                break
            h = (h + 1) % self.size
        if self.slots[h] is None:
            self.count += 1
            self.slots[h] = (self.key, self.value)

    # A operation function for get data from hash table
    def get(self, key):
        h = self._hash(key)
        while self.slots[h] is not None:
            if self.slots[h][0] is key:
                return self.slots[h][-1]
            h = (h + 1) % self.size
        if self.slots[h] is None:
            return None