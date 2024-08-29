class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.recent = Node(0, 0)
        self.lru = Node(0, 0)
        self.recent.prev = self.lru
        self.lru.next = self.recent
        self.max_capacity = capacity
        self.curr_capacity = 0
        self.dict = {}

    def _remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_recent(self, node):
        most_recent = self.recent.prev
        most_recent.next = node
        node.prev = most_recent
        node.next = self.recent
        self.recent.prev = node

    def get(self, key: int) -> int:
        if key in self.dict:
            node = self.dict[key]
            self._remove(node)
            self._add_to_recent(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            node = self.dict[key]
            node.val = value
            self._remove(node)
            self._add_to_recent(node)
        else:
            if self.curr_capacity == self.max_capacity:
                lru_node = self.lru.next
                self._remove(lru_node)
                del self.dict[lru_node.key]
                self.curr_capacity -= 1
            new_node = Node(key, value)
            self.dict[key] = new_node
            self._add_to_recent(new_node)
            self.curr_capacity += 1