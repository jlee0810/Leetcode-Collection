class Solution:
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def isLandCell(self, row, col, grid):
        return grid[row][col] == 1

    def isSubIsland(self, row, col, grid1, grid2, visited):
        total_rows = len(grid2)
        total_cols = len(grid2[0])

        is_sub_island = True

        pending_cells = deque()
        pending_cells.append((row, col))
        visited[row][col] = True

        while pending_cells:
            curr_row, curr_col = pending_cells.popleft()

            if not self.isLandCell(curr_row, curr_col, grid1):
                is_sub_island = False

            for direction in self.directions:
                next_row = curr_row + direction[0]
                next_col = curr_col + direction[1]
                if (
                    0 <= next_row < total_rows
                    and 0 <= next_col < total_cols
                    and not visited[next_row][next_col]
                    and self.isLandCell(next_row, next_col, grid2)
                ):
                    pending_cells.append((next_row, next_col))
                    visited[next_row][next_col] = True
        return is_sub_island

    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        total_rows = len(grid2)
        total_cols = len(grid2[0])

        visited = [[False] * total_cols for _ in range(total_rows)]
        sub_island_count = 0

        for row in range(total_rows):
            for col in range(total_cols):
                if (
                    not visited[row][col]
                    and self.isLandCell(row, col, grid2)
                    and self.isSubIsland(row, col, grid1, grid2, visited)
                ):
                    sub_island_count += 1

        return sub_island_count
