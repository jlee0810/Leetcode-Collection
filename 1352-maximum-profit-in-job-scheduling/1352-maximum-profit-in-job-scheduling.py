class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        cache = {}

        intervals = []
        for start, end, p in zip(startTime, endTime, profit):
            intervals.append([start, end, p])
        intervals.sort()
        print(intervals)

        def dp(i):
            if i == len(startTime):
                return 0
            if i in cache:
                return cache[i]
            most_profit = dp(i + 1)
            next_avail_idx = bisect.bisect_left(intervals, [intervals[i][1], 0, 0])
            most_profit = max(most_profit, dp(next_avail_idx) + intervals[i][2])

            cache[i] = most_profit
            return most_profit

        return dp(0)