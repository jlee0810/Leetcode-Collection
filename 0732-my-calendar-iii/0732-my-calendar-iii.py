class MyCalendarThree:
    def __init__(self):
        self.times = defaultdict(int)
        
    def book(self, startTime: int, endTime: int) -> int:
        self.times[startTime] += 1
        self.times[endTime] -= 1

        max_intersect = 0
        intersect = 0

        for t in sorted(self.times):
            intersect += self.times[t]
            max_intersect = max(max_intersect, intersect)
        
        return max_intersect


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)