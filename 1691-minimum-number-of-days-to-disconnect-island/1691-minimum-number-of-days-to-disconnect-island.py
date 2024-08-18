class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        def bfs(r, c, temp_grid):
            q = deque()
            q.append((r, c))
            temp_grid[r][c] = 0
            
            while q:
                curr_r, curr_c = q.popleft()
                for dr, dc in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    nr, nc = curr_r + dr, curr_c + dc
                    if 0 <= nr < len(temp_grid) and 0 <= nc < len(temp_grid[0]) and temp_grid[nr][nc] == 1:
                        temp_grid[nr][nc] = 0
                        q.append((nr, nc))
                        
        def count_islands(temp_grid):
            count = 0
            for i in range(len(temp_grid)):
                for j in range(len(temp_grid[0])):
                    if temp_grid[i][j] == 1:
                        bfs(i, j, temp_grid)
                        count += 1
            return count

        if count_islands(deepcopy(grid)) != 1:
            return 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if count_islands([row[:] for row in grid]) != 1:
                        return 1
                    grid[i][j] = 1

        return 2
