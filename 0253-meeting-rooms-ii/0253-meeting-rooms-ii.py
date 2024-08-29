class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        rooms = 0
        min_heap = []

        for interval in intervals:
            if min_heap and min_heap[0] <= interval[0]:
                heappop(min_heap)
                heappush(min_heap, interval[1])
            else:
                heappush(min_heap, interval[1])
                room = max(rooms, len(min_heap))
        
        return room