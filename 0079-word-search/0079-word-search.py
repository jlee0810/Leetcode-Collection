class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])
        visited = set()

        def backtrack(idx, r, c):
            if idx == len(word):
                return True
            if (r, c) in visited or r < 0 or r >= row or c < 0 or c >= col or word[idx] != board[r][c]:
                return False
            visited.add((r, c))
            exists = backtrack(idx + 1, r + 1, c) or backtrack(idx + 1, r - 1, c) or backtrack(idx + 1, r, c + 1) or backtrack(idx + 1, r, c - 1)
            visited.remove((r, c))
            return exists

        
        for i in range(row):
            for j in range(col):
                if backtrack(0, i, j):
                    return True
        return False
