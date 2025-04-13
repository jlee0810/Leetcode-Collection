class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0

        def bfs(r, c):
            nonlocal max_area
            q = deque()
            q.append((r, c))
            area = 0
            grid[r][c] = 0

            while q:
                curr_r, curr_c = q.popleft()
                area += 1
                for dr, dc in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    nr, nc = curr_r + dr, curr_c + dc
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] != 0:
                        q.append((nr, nc))
                        grid[nr][nc] = 0

            max_area = max(max_area, area)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    bfs(i, j)
        
        return max_area