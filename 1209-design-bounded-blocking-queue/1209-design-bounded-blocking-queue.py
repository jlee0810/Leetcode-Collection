from collections import deque
import threading

class BoundedBlockingQueue(object):
    def __init__(self, capacity: int):
        self.cond = threading.Condition()
        self.q = deque()
        self.capacity = capacity

    def enqueue(self, element: int) -> None:
        with self.cond:
            while len(self.q) >= self.capacity:
                self.cond.wait()
            self.q.append(element)
            self.cond.notify_all()
        

    def dequeue(self) -> int:
        with self.cond:
            while len(self.q) == 0:
                self.cond.wait()
            element = self.q.popleft()
            self.cond.notify_all()
            return element

    def size(self) -> int:
        with self.cond:
            return len(self.q)