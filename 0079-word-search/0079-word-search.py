class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(r, c, idx, visited):
            if idx == len(word):
                return True
            if (r, c) in visited or r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or board[r][c] != word[idx]:
                return False
            
            visited.add((r, c))
            for dr, dc in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if dfs(nr, nc, idx + 1, visited):
                    return True
            visited.remove((r, c))
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    visited = set()
                    if dfs(i, j, 0, visited):
                        return True

        return False


