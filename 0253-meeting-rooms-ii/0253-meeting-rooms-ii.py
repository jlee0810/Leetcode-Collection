class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # intervals.sort()
        # rooms = 0
        # min_heap = []

        # for interval in intervals:
        #     if min_heap and min_heap[0] <= interval[0]:
        #         heappop(min_heap)
        #         heappush(min_heap, interval[1])
        #     else:
        #         heappush(min_heap, interval[1])
        #         room = max(rooms, len(min_heap))
        
        # return room
        
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
