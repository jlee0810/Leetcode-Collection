class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        flow_grid = [
            [set() for _ in range(len(heights[0]))] for _ in range(len(heights))
        ]

        def bfs(i, j, ispacific):
            nonlocal flow_grid

            q = deque()
            q.append((i, j))
            visited = set()
            visited.add((i, j))

            while q:
                curr_r, curr_c = q.popleft()
                if ispacific:
                    flow_grid[curr_r][curr_c].add("p")
                else:
                    flow_grid[curr_r][curr_c].add("a")

                for dr, dc in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                    nr, nc = curr_r + dr, curr_c + dc
                    if (
                        0 <= nr < len(heights)
                        and 0 <= nc < len(heights[0])
                        and (nr, nc) not in visited
                        and heights[nr][nc] >= heights[curr_r][curr_c]
                    ):
                        visited.add((nr, nc))
                        q.append((nr, nc))

        for col in range(len(heights[0])):
            bfs(0, col, True)
            bfs(len(heights) - 1, col, False)
        for row in range(len(heights)):
            bfs(row, 0, True)
            bfs(row, len(heights[0]) - 1, False)

        result = []
        for r in range(len(flow_grid)):
            for c in range(len(flow_grid[0])):
                if len(flow_grid[r][c]) == 2:
                    result.append([r, c])
        
        return result