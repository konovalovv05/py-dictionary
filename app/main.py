class Node:
    def __init__(self, key, value, hash_value):
        self.key = key
        self.value = value
        self.hash = hash_value


class Dictionary:
    def __init__(self, capacity = 2):
        if capacity < 1:
            capacity = 2


        self.capacity = capacity
        self.size = 0
        self.load_factor = 0.75
        self.buckets = [ [] for _ in range(self.capacity)]

    def _get_index(self, key_hash):
        return key_hash % self.capacity

    def __setitem__(self, key, value):
        key_hash = hash(key)
        index = self._get_index(key_hash)
        bucket = self.buckets[index]

        for node in bucket:
            if node.hash == key_hash and node.key == key:
                node.value = value
                return
        bucket.append(Node(key, value, key_hash))
        self.size += 1

        if self.size / self.capacity > self.load_factor:
            self._resize()

    def __getitem__(self, key):
        key_hash = hash(key)
        index = self._get_index(key_hash)
        bucket = self.buckets[index]

        for node in bucket:
            if node.hash == key_hash and node.key == key:
                return node.value

        raise KeyError(f"Key {key} not found")

    def __len__(self):
        return self.size

    def _resize(self):
        old_buckets = self.buckets
        self.capacity *= 2
        self.buckets = [ [] for _ in range(self.capacity)]
        self.size = 0

        for bucket in old_buckets:
            for node in bucket:
                self[node.key] = node.value


