# HashTable: An unordered key-value data structure providing O(1) store, retrieve
# search and delete operations.
# Your implementation should pass the tests in test_hash_table.py.
# Nick Morris


class HashTable():
    
    def __init__(self, ele=10):
        self.size = ele
