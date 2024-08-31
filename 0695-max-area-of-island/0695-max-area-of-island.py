class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        
        def bfs(r, c):
            nonlocal max_area
            q = deque([(r, c)])
            area = 0
            grid[r][c] = 0

            while q:
                curr_r, curr_c = q.popleft()
                area += 1
                for dr, dc in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    new_r, new_c = curr_r + dr, curr_c + dc
                    if 0 <= new_r < len(grid) and 0 <= new_c < len(grid[0]) and grid[new_r][new_c] == 1:
                        q.append((new_r, new_c))
                        grid[new_r][new_c] = 0
            max_area = max(max_area, area)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    bfs(i, j)

        return max_area