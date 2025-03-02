class Node:
    def __init__(self):
        self.val = None
        self.next = None
        self.prev = None
        self.key = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.lru = Node()
        self.recent = Node()
        self.lru.next = self.recent
        self.recent.prev = self.lru
        self.size = 0

    def remove(self, key):
        node = self.map[key]
        del self.map[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

    def add(self, key, val):
        new_node = Node()
        new_node.val = val
        new_node.key = key
        self.map[key] = new_node
        self.recent.prev.next = new_node
        new_node.prev = self.recent.prev
        new_node.next = self.recent
        self.recent.prev = new_node
        self.size += 1

    def get(self, key: int) -> int:
        if key in self.map:
            val = self.map[key].val
            self.remove(key)
            self.add(key, val)
            return val
        return -1


    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.remove(key)
            self.add(key, value)
        else:
            if self.size == self.capacity:
                self.remove(self.lru.next.key)
            self.add(key, value)



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)