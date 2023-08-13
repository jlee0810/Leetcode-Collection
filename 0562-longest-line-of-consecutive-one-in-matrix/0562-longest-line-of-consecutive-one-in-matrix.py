class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        maxLen = 0
        dp = [[[0,0,0,0]for _ in range(len(mat[0]))] for _ in range(len(mat))]

        ROW, COL = len(mat), len(mat[0])
        for i in range(ROW):
            for j in range(COL):
                if mat[i][j] == 1:
                    dp[i][j][0] = dp[i][j-1][0] + 1 if j > 0 else 1
                    dp[i][j][1] = dp[i-1][j][1] + 1 if i > 0 else 1
                    dp[i][j][2] = dp[i-1][j-1][2] + 1 if i > 0 and j > 0 else 1
                    dp[i][j][3] = dp[i-1][j+1][3] + 1 if i > 0 and j < COL-1 else 1
                    maxLen = max(maxLen, dp[i][j][0], dp[i][j][1], dp[i][j][2], dp[i][j][3])
        return maxLen
