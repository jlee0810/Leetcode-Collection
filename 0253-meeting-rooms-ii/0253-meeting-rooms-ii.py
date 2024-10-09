class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        time = defaultdict(int)

        for startTime, endTime in intervals:
            time[startTime] += 1
            time[endTime] -= 1
        
        max_intersect = 0
        intersect = 0

        for t in sorted(time):
            intersect += time[t]
            max_intersect = max(max_intersect, intersect)
        
        return max_intersect
