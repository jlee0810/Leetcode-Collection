class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        op = 0

        for c in range(len(grid[0])):
            last_val = grid[0][c]
            for r in range(1, len(grid)):
                while grid[r][c] <= last_val:
                    op += 1
                    grid[r][c] += 1
                last_val = grid[r][c]
        
        return op