class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            points, skip = questions[i]
            next_question = i + skip + 1
            solve = points + (dp[next_question] if next_question < n else 0)
            skip_question = dp[i + 1]
            dp[i] = max(solve, skip_question)

        return dp[0]