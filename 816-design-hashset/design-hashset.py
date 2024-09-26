class MyHashSet:

    def __init__(self):
        self.buckets = [None] * 1000  # Adjust the initial size as needed

    def hash_function(self, key):
        # Simple hash function (can be replaced with a more complex one)
        return key % len(self.buckets)

    def add(self, key: int) -> None:
        index = self.hash_function(key)
        if not self.buckets[index]:
            self.buckets[index] = set()
        self.buckets[index].add(key)

    def remove(self, key: int) -> None:
        index = self.hash_function(key)
        if self.buckets[index] and key in self.buckets[index]:
            self.buckets[index].remove(key)

    def contains(self, key: int) -> bool:
        index = self.hash_function(key)
        return self.buckets[index] and key in self.buckets[index]