class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        min_erase = 0
        prev_end = float('-inf')
        intervals.sort(key = lambda x : x[1])

        for start, end in intervals:
            if start >= prev_end:
                prev_end = end
            else:
                min_erase += 1
        
        return min_erase