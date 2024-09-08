from sortedcontainers import SortedList

class MyCalendarTwo:
    def __init__(self):
        self.calendar = SortedList()
        self.overlaps = SortedList()

    def book(self, start: int, end: int) -> bool:
        for o_start, o_end in self.overlaps:
            if start < o_end and end > o_start:
                return False

        for c_start, c_end in self.calendar:
            if start < c_end and end > c_start:
                overlap_start = max(start, c_start)
                overlap_end = min(end, c_end)
                self.overlaps.add((overlap_start, overlap_end))
        
        self.calendar.add((start, end))
        return True

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)