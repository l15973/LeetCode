# Implement hash table where collisions are handled using linear probing.

class LinearProbing():
    def __init__(self, LENGTH_OF_ARR = 10):
        self.length = LENGTH_OF_ARR
        self.arr = [None for i in range(LENGTH_OF_ARR)]
        self.new_info = {}

    def get_hash(self, key) -> int:
        sum_code = 0
        for chr in key:
            sum_code += ord(chr)
        number = sum_code % self.length
        return number

    def __setitem__(self, key, value):
        if self.length == len(self.new_info):
            raise Exception("Hashmap full")
        index = self.get_hash(key)
        while self.arr[index]:
            if self.arr[index][0] == key:
                break
            if index == self.length-1:
                index = 0 
            else:
                index += 1
        self.arr[index] = (key, value)
        self.new_info[key] = index

    def __getitem__(self, key):
        if key not in self.new_info:
            return ""
        index = self.new_info[key]
        return self.arr[index][1]


    def __delitem__(self, key):
        index = self.new_info[key]
        self.arr[index] = None
        del self.new_info[key]

n = LinearProbing()
n["march 6"] = 20
n["march 17"] =  88
print(n.arr)
# [('march 17', 88), None, None, None, None, None, None, None, None, ('march 6', 20)]

n["march 17"] = 29
print(n.arr)
# [('march 17', 29), None, None, None, None, None, None, None, None, ('march 6', 20)]

n["nov 1"] = 1
print(n.arr)
# [('march 17', 29), ('nov 1', 1), None, None, None, None, None, None, None, ('march 6', 20)]

n["march 33"] = 234
print(n.arr)
# [('march 17', 29), ('nov 1', 1), None, None, None, None, None, ('march 33', 234), None, ('march 6', 20)]

print(n["dec 1"])
# no result

print(n["march 33"])
# 234

n["march 33"] = 999
print(n.arr)
# [('march 17', 29), ('nov 1', 1), None, None, None, None, None, ('march 33', 999), None, ('march 6', 20)]

print(n["march 33"])

n["april 1"]=87
print(n.arr)
# [('march 17', 29), ('nov 1', 1), None, None, None, None, None, ('march 33', 999), ('april 1', 87), ('march 6', 20)]


n["april 2"]=123
print(n.arr)
# [('march 17', 29), ('nov 1', 1), ('april 2', 123), None, None, None, None, ('march 33', 999), ('april 1', 87), ('march 6', 20)]

n["april 3"]=234234
print(n.arr)
# [('march 17', 29), ('nov 1', 1), ('april 2', 123), ('april 3', 234234), None, None, None, ('march 33', 999), ('april 1', 87), ('march 6', 20)]

n["april 4"]=91
print(n.arr)
# [('march 17', 29), ('nov 1', 1), ('april 2', 123), ('april 3', 234234), ('april 4', 91), None, None, ('march 33', 999), ('april 1', 87), ('march 6', 20)]

n["May 22"]=4
print(n.arr)
# [('march 17', 29), ('nov 1', 1), ('april 2', 123), ('april 3', 234234), ('april 4', 91), ('May 22', 4), None, ('march 33', 999), ('april 1', 87), ('march 6', 20)]

n["May 7"]=47
print(n.arr)
# [('march 17', 29), ('nov 1', 1), ('april 2', 123), ('april 3', 234234), ('april 4', 91), ('May 22', 4), ('May 7', 47), ('march 33', 999), ('april 1', 87), ('march 6', 20)]


# n["Jan 1"]=0
print(n.arr)
# Exception: Hashmap full

del n["april 2"]
print(n.arr)
# [('march 17', 29), ('nov 1', 1), None, ('april 3', 234234), ('april 4', 91), ('May 22', 4), ('May 7', 47), ('march 33', 999), ('april 1', 87), ('march 6', 20)]

n["Jan 1"]=0
print(n.arr)
# [('march 17', 29), ('nov 1', 1), ('Jan 1', 0), ('april 3', 234234), ('april 4', 91), ('May 22', 4), ('May 7', 47), ('march 33', 999), ('april 1', 87), ('march 6', 20)]