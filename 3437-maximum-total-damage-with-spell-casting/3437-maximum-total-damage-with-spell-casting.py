class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        freq = Counter(power)
        keys = list(sorted(set(power)))

        dp = [0 for _ in range(len(keys))]

        for i in range(len(keys)):
            dp[i] = 0
            if i - 4 >= 0:
                dp[i - 3] = max(dp[i - 3], dp[i - 4])
            for j in range(1, 4):
                if i - j >= 0 and keys[i] - keys[i - j] > 2:
                    dp[i] = max(dp[i], dp[i - j])
            dp[i] += freq[keys[i]] * keys[i]

        return max(dp)