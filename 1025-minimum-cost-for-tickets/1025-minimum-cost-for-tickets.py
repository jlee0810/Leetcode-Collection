class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        days_set = set(days)
        last_day = days[-1]

        dp = [0] * (last_day + 1)

        for day in range(1, last_day + 1):
            if day not in days_set:
                dp[day] = dp[day - 1]
                continue

            cost1 = dp[day - 1] + costs[0]
            cost2 = dp[max(0, day - 7)] + costs[1]
            cost3 = dp[max(0, day - 30)] + costs[2]

            dp[day] = min(cost1, cost2, cost3)

        return dp[last_day]
