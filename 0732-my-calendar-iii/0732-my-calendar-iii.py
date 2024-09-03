class MyCalendarThree:

    def __init__(self):
        self.time = defaultdict(int)
        

    def book(self, startTime: int, endTime: int) -> int:
        intersect = 0
        self.time[startTime] += 1
        self.time[endTime] -= 1

        max_intersect = 0
        intersect = 0

        for time in sorted(self.time):
            intersect += self.time[time]
            max_intersect = max(max_intersect, intersect)
        
        return max_intersect


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)