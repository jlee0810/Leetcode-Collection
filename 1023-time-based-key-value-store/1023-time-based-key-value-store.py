class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        result = ""
        values = self.timemap[key]
        l, r = 0, len(values) - 1

        while l <= r:
            mid = (l + r) // 2
            if values[mid][0] <= timestamp: 
                result = values[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        return result

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)