class Node:
    def __init__(self, key, value):
        self.prev = self.next = None
        self.key, self.value = key, value

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.lru, self.recent = Node(0, 0), Node(0, 0)
        self.lru.next = self.recent
        self.recent.prev = self.lru

    def insert(self, node):
        most_recent = self.recent.prev
        node.prev = most_recent
        node.next = self.recent
        most_recent.next = node
        self.recent.prev = node
    
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value

        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache.values()) > self.capacity:
            lru = self.lru.next
            self.remove(lru)
            del self.cache[lru.key]
        
    
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)