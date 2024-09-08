class MyCalendarTwo:
    def __init__(self):
        self.times = defaultdict(int)
        
    def book(self, startTime: int, endTime: int) -> int:
        self.times[startTime] += 1
        self.times[endTime] -= 1

        intersect = 0

        for t in sorted(self.times):
            intersect += self.times[t]
            if intersect >= 3:
                self.times[startTime] -= 1
                self.times[endTime] += 1
                return False
        return True



# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)