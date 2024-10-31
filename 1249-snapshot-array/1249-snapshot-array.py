class SnapshotArray:

    def __init__(self, length: int):
        self.snapshot = [[[0, 0]] for _ in range(length)]
        self.snapid = 0
        
    def set(self, index: int, val: int) -> None:
        self.snapshot[index].append([self.snapid, val])

    def snap(self) -> int:
        self.snapid += 1
        return self.snapid - 1

    def get(self, index: int, snap_id: int) -> int:
        snap_index = bisect.bisect_right(self.snapshot[index], [snap_id, float('inf')])
        return self.snapshot[index][snap_index - 1][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)