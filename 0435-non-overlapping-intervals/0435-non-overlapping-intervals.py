class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        prev_end = float('-inf')
        intervals.sort(key = lambda x : x[1])

        erase = 0
        for interval in intervals:
            if interval[0] < prev_end:
                erase += 1
            else:
                prev_end = interval[1]
        
        return erase