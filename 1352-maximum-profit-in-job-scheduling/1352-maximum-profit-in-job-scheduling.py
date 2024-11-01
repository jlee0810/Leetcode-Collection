class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        cache = {}

        intervals = [[start, end, p] for start, end, p in zip(startTime, endTime, profit)]
        intervals.sort()
        
        def dp(i):
            if i == len(startTime):
                return 0
            if i in cache:
                return cache[i]
            
            best_profit = dp(i + 1) #skip i
            next_avail_idx = bisect.bisect_left(intervals, [intervals[i][1], 0, 0])
            best_profit = max(best_profit, dp(next_avail_idx) + intervals[i][2])

            cache[i] = best_profit
            return best_profit 

        return dp(0)