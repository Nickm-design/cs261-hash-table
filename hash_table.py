# HashTable: An unordered key-value data structure providing O(1) store, retrieve
# search and delete operations.
# Your implementation should pass the tests in test_hash_table.py.
# Nick Morris


class HashTable():
    
    def __init__(self, size=10):
        self.size = size
        self.data = {None for x in range(0, size)}
    
    def __setitem__(self, idx, value):
        return idx, value
    
    def __getitem__(self,idx):
        return idx