class Node:
    def __init__(self, key = None, val = None):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.lru = Node()
        self.recent = Node()
        self.lru.next = self.recent
        self.recent.prev = self.lru
        self.capacity = capacity
        self.size = 0
        self.map = {}

    def add_to_recent(self, node):
        old_recent = self.recent.prev
        old_recent.next = node
        node.prev = old_recent
        node.next = self.recent
        self.recent.prev = node

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map[key]
            self.remove_node(node)
            self.add_to_recent(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            self.remove_node(node)
            node.val = value
            self.add_to_recent(node)
        else:
            if self.capacity == self.size:
                lru_node = self.lru.next
                self.remove_node(lru_node)
                del self.map[lru_node.key]
                self.size -= 1
            new = Node(key, value)
            self.map[key] = new
            self.add_to_recent(new)
            self.size += 1

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)