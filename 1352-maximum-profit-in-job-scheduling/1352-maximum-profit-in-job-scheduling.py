class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        intervals = [[start, end, profit] for start, end, profit in zip(startTime, endTime, profit)]
        intervals.sort()

        cache = {}

        def dp(i):
            if i == len(startTime):
                return 0
            if i in cache:
                return cache[i]
            result = dp(i + 1)
            next_interval = bisect.bisect_right(intervals, [intervals[i][1], 0, 0])
            result = max(result, dp(next_interval) + intervals[i][2])
            cache[i] = result
            return result

        return dp(0)