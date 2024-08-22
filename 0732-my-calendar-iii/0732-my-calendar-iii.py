from sortedcontainers import SortedDict
class MyCalendarThree:
    def __init__(self):
        self.times = defaultdict(int)

    def book(self, start: int, end: int) -> int:
        self.times[start] += 1
        self.times[end] -= 1

        ans = 0
        curr_inter = 0

        for t in sorted(self.times):
            curr_inter += self.times[t]
            ans = max(ans, curr_inter)
        
        return ans


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)