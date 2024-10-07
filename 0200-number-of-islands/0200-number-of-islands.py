class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(r, c):
            q = deque()
            q.append((r, c))
            grid[r][c] = "0"

            while q:
                curr_r, curr_c = q.popleft()
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = curr_r + dr, curr_c + dc

                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == "1":
                        q.append((nr, nc))
                        grid[nr][nc] = "0"
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    bfs(i, j)
                    count += 1
        
        return count