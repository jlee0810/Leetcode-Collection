class Solution:
    def firstDayBeenInAllRooms(self, nextVisit: List[int]) -> int:
        n = len(nextVisit)
        dp = [0 for _ in range(n)]
        for e, i in enumerate(nextVisit[:-1], 1):
            dp[e] = dp[e - 1] + 1
            dp[e] = (2 * dp[e] - dp[i]) % (10 ** 9 + 7)
        return dp[-1]