class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        key_hash = self.hash_function(key)
        key_value = [key, value]

        if self.table[key_hash] is None:
            self.table[key_hash] = list([key_value])
            return True

        for pair in self.table[key_hash]:
            if pair[0] == key:
                pair[1] = value
                return True

        self.table[key_hash].append(key_value)
        return True

    def get(self, key):
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for index in range(len(self.table[key_hash])):
                if self.table[key_hash][index][0] == key:
                    self.table[key_hash].pop(index)
                    return 'Item removed'
        return 'Item not found'


if __name__ == '__main__':
    H = HashTable(3)
    H.insert("car", 10)
    H.insert("tree", 20)
    H.insert("sky", 30)
    print(H.table)
    print(H.delete("sky"))
    print(H.table)
    