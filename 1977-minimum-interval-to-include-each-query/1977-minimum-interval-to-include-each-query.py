class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        dic = {}
        min_heap = []
        intervals.sort()
        i = 0

        for query in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= query:
                l, r = intervals[i]
                heappush(min_heap, (r - l + 1, r))
                i += 1
            
            while min_heap and min_heap[0][1] < query:
                heappop(min_heap)
            dic[query] = min_heap[0][0] if min_heap else -1
        
        result = []
        for query in queries:
            result.append(dic[query])
        
        return result
            