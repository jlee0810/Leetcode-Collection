class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        results = []
        cols = [-1 for _ in range(n)]
        
        def can_place(row, col):
            for i in range(row):
                if cols[i] == col or abs(i - row) == abs(cols[i] - col):
                    return False
            return True
        
        def backtrack(row):
            if row == n:
                results.append(cols.copy())
                return
            for col in range(n):
                if can_place(row, col):
                    cols[row] = col
                    backtrack(row + 1)
                    cols[row] = -1
        
        backtrack(0)

        for result in results:
            for i in range(n):
                result[i] = "." * result[i] + 'Q' + '.' * (n - result[i] - 1)
        
        return results