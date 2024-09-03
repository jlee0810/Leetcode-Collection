class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        idx = 0
        intervals.sort()
        dic = {}
        min_heap = []

        for query in sorted(queries):
            while idx < len(intervals) and intervals[idx][0] <= query:
                l, r = intervals[idx]
                heappush(min_heap, (r - l + 1, r))
                idx += 1

            while min_heap and min_heap[0][1] < query:
                heappop(min_heap)
            
            dic[query] = min_heap[0][0] if min_heap else -1

        result = []
        for query in queries:
            result.append(dic[query])
        
        return result