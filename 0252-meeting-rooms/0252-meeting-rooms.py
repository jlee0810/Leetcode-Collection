class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        if not intervals:
            return True
        last_meet = intervals[0][1]

        for i in range(1, len(intervals)):
            if intervals[i][0] < last_meet:
                return False
            else:
                last_meet = intervals[i][1]

        return True