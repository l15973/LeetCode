# !! Dictionary is the python specific implementation of the hash table !!
# Look up by key is O(1)
# insertion / deletion by key is O(1)
class HashTable:
    def __init__(self, LENGTH_OF_ARRAY=10):
        self.length = LENGTH_OF_ARRAY
        self.arr = [None for i in range(LENGTH_OF_ARRAY)]

    def get_hash(self, key) -> int:
        sum_code = 0
        for chr in key:
            sum_code += ord(chr)
        number = sum_code % self.length
        return number

    def __getitem__(self, key):
        index = self.get_hash(key)
        return self.arr[index]
    def __setitem__(self, key, value):
        index = self.get_hash(key)
        self.arr[index] = value

    def __delitem__(self, key):
        index = self.get_hash(key) 
        self.arr[index] = None
    
h = HashTable()
h['march 6'] = 120
h['dec 21'] = 98
h['march 1'] = 110
h['march 5'] = 150
h['march 4'] = 140
print(h.arr)
# [None, 98, None, None, 110, None, None, 140, 150, 120]

print(h['march 6'])
# 120

del h['march 6']
print(h.arr)
# [None, 98, None, None, 110, None, None, 140, 150, None]