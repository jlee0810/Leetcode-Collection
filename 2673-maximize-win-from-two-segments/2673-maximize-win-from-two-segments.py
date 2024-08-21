class Solution:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        n = len(prizePositions)
        dp = [0] * (n + 1)
        max_prizes = 0
        
        j = 0
        for i in range(n):
            while prizePositions[i] - prizePositions[j] > k:
                j += 1
            
            current_prizes = i - j + 1
            dp[i + 1] = max(dp[i], current_prizes)
            max_prizes = max(max_prizes, current_prizes + dp[j])
        
        return max_prizes