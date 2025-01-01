class Solution:
    def maxScore(self, s: str) -> int:
        zero_count = [0] * (len(s) - 1)
        one_count = [0] * (len(s) - 1)

        for i in range(len(s) - 1):
            if s[i] == '0':
                zero_count[i] = zero_count[i - 1] + 1
            else:
                zero_count[i] = zero_count[i - 1]

        s = s[::-1]

        for i in range(len(s) - 1):
            if s[i] == '1':
                one_count[i] = one_count[i - 1] + 1
            else:
                one_count[i] = one_count[i - 1]
        one_count = one_count[::-1]

        max_score = 0
        for i in range(len(s) - 1):
            max_score = max(max_score, zero_count[i] + one_count[i])
        
        return max_score
