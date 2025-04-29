class Node:
    def __init__(self):
        self.key = None
        self.val = None
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.lru = Node()
        self.recent = Node()
        self.lru.next = self.recent
        self.recent.prev = self.lru
        self.map = {}

    def add(self, key, val):
        new = Node()
        new.key = key
        new.val = val
        self.map[key] = new
        self.recent.prev.next = new
        new.prev = self.recent.prev
        new.next = self.recent
        self.recent.prev = new
        self.size += 1

    def delete(self, key):
        old = self.map[key]
        del self.map[key]
        self.size -= 1

        old.prev.next = old.next
        old.next.prev = old.prev

    def get(self, key):
        if key in self.map:
            node = self.map[key]
            self.delete(key)
            self.add(key, node.val)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.delete(key)
            self.add(key, value)
        else:
            if self.size >= self.capacity:
                self.delete(self.lru.next.key)
            self.add(key, value)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
