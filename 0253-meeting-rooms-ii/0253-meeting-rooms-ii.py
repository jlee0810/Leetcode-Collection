class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        min_heap = []
        intervals.sort()
        room = 0 

        for interval in intervals:
            if min_heap and min_heap[0] <= interval[0]:
                heappop(min_heap)
                heappush(min_heap, interval[1])
            else:
                heappush(min_heap, interval[1])
                room = max(room, len(min_heap))
        
        return room