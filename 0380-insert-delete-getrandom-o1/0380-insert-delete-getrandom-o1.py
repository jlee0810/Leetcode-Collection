class RandomizedSet:
    def __init__(self):
        self.rset = []
        self.idx = {}

    def insert(self, val: int) -> bool:
        if val in self.idx:
            return False
        else:
            self.idx[val] = len(self.rset)
            self.rset.append(val)
            return True

    def remove(self, val: int) -> bool:
        if val in self.idx:
            idx = self.idx[val]
            last_val = self.rset[-1]
            self.rset[idx], self.rset[-1] = self.rset[-1], self.rset[idx]
            self.idx[last_val] = idx
            self.rset.pop()
            del self.idx[val]
            return True
        return False

    def getRandom(self) -> int:
        rand_idx = random.randint(0, len(self.rset) - 1)
        return self.rset[rand_idx]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()