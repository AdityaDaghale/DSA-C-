"""Hash Table - Dictionary Implementation"""

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size
    
    def hash_function(self, key):
        return hash(key) % self.size
    
    def insert(self, key, value):
        idx = self.hash_function(key)
        if self.table[idx] is None:
            self.table[idx] = []
        for i, (k, v) in enumerate(self.table[idx]):
            if k == key:
                self.table[idx][i] = (key, value)
                return
        self.table[idx].append((key, value))
    
    def search(self, key):
        idx = self.hash_function(key)
        if self.table[idx]:
            for k, v in self.table[idx]:
                if k == key:
                    return v
        return None
    
    def delete(self, key):
        idx = self.hash_function(key)
        if self.table[idx]:
            self.table[idx] = [(k, v) for k, v in self.table[idx] if k != key]

if __name__ == "__main__":
    ht = HashTable()
    ht.insert("name", "Aditya")
    ht.insert("age", 25)
    ht.insert("city", "Delhi")
    print("Search 'name':", ht.search("name"))
    print("Search 'age':", ht.search("age"))
