class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        last_end = -1000000
        for interval in intervals:
            if interval[0] < last_end:
                return False
            last_end = interval[1]

        return True