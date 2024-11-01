class SnapshotArray:

    def __init__(self, length: int):
        self.snapshot = [[[0, 0]] for _ in range(length)]
        self.snapId = 0

    def set(self, index: int, val: int) -> None:
        self.snapshot[index].append([self.snapId, val])

    def snap(self) -> int:
        self.snapId += 1
        return self.snapId - 1
        
    def get(self, index: int, snap_id: int) -> int:
        snapIdx = bisect.bisect_left(self.snapshot[index], [snap_id, float('inf')])
        print(snapIdx)
        return self.snapshot[index][snapIdx - 1][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)