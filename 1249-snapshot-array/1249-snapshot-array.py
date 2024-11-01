class SnapshotArray:

    def __init__(self, length: int):
        self.snapshot = [[[0, 0]] for _ in range (length)] 
        self.snap_id = 0   

    def set(self, index: int, val: int) -> None:
        self.snapshot[index].append([self.snap_id, val])       

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        snap_idx = bisect.bisect_left(self.snapshot[index], [snap_id, float('inf')])
        return self.snapshot[index][snap_idx - 1][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)