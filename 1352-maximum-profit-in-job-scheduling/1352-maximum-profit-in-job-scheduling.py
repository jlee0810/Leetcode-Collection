class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        cache = {}

        intervals = sorted(zip(startTime, endTime, profit), key=lambda x: x[0])

        def b_search(curr_end):
            result = len(intervals)
            start, end = 0, len(intervals) - 1
            while start <= end:
                mid = (start + end) // 2
                if intervals[mid][0] >= curr_end:
                    result = mid
                    end = mid - 1
                else:
                    start = mid + 1
            return result

        def dp(i):
            if i == len(intervals):
                return 0
            if i in cache:
                return cache[i]
            
            bestProfit = dp(i + 1)
            
            next_avail_idx = b_search(intervals[i][1])
            bestProfit = max(bestProfit, dp(next_avail_idx) + intervals[i][2])
            
            cache[i] = bestProfit
            return cache[i]
        
        return dp(0)
