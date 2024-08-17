class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        rows, cols = len(points), len(points[0])
        dp = points[0]

        for r in range(1, rows):
            left_dp = [0] * cols
            right_dp = [0] * cols

            left_dp[0] = dp[0]
            for c in range(1, cols):
                left_dp[c] = max(left_dp[c - 1] - 1, dp[c])

            right_dp[cols - 1] = dp[cols - 1]
            for c in range(cols - 2, -1, -1):
                right_dp[c] = max(right_dp[c + 1] - 1, dp[c])

            for c in range(cols):
                dp[c] = points[r][c] + max(left_dp[c], right_dp[c])

        return max(dp)

        # max_points = 0

        # def backtrack(row, col, total):
        #     nonlocal max_points
        #     if row == len(points):
        #         max_points = max(max_points, total)
        #         return
        #     for i in range(len(points[0])):
        #         new_total = total + points[row][i] - abs(col - i)
        #         backtrack(row + 1, i, new_total)

        # for i in range(len(points[0])):
        #     backtrack(1, i, points[0][i])

        # return max_points
