# Collision Handling
# Solution: Seperate Chaining

class HashTable:
    def __init__(self, LENGTH_OF_ARRAY=10):
        self.length = LENGTH_OF_ARRAY
        self.arr = [ [] for i in range(LENGTH_OF_ARRAY) ]

    def get_hash(self, key) -> int:
        sum_code = 0
        for chr in key:
            sum_code += ord(chr)
        number = sum_code % self.length
        return number

    def __getitem__(self, key):
        index = self.get_hash(key)
        for e in self.arr[index]:
            if e[0] == key:
                return e[1]
    def __setitem__(self, key, value):
        index = self.get_hash(key)
        found_exists = False
        for i, element in enumerate(self.arr[index]):
            if key == element[0]:
                self.arr[index][i] = value
                found_exists = True
        if not found_exists:
            self.arr[index].append((key, value))

    def __delitem__(self, key):
        index = self.get_hash(key) 
        for i, element in enumerate(self.arr[index]):
            if key == element[0]:
                del self.arr[index][i]
    
h = HashTable()
h['march 6'] = 120
h['dec 21'] = 98
h['march 1'] = 110
h['march 5'] = 150
h['march 4'] = 140
h['march 17'] = 170
print(h.arr)
# [[], [('dec 21', 98)], [], [], [('march 1', 110)], [], [], [('march 4', 140)], [('march 5', 150)], [('march 6', 120), ('march 17', 170)]]


del h['dec 21']
print(h.arr)
# [[], [], [], [], [('march 1', 110)], [], [], [('march 4', 140)], [('march 5', 150)], [('march 6', 120), ('march 17', 170)]]
del h['march 17']
print(h.arr)
# [[], [], [], [], [('march 1', 110)], [], [], [('march 4', 140)], [('march 5', 150)], [('march 6', 120)]]