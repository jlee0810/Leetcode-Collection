class Solution:
    def maxTrailingZeros(self, grid: list[list[int]]) -> int:
        m, n = len(grid)+1, len(grid[0])+1
        grid = [[(0,0,0,0)]*n]+[[(0,0,0,0)]+row for row in grid]

        def prefix_sum(row,col):
            val = grid[row][col]
            factor_2, factor_5 = 0, 0

            while val > 0:
                if val%2: 
                    break
                val//= 2
                factor_2 += 1
   
            while val > 0:
                if val%5: 
                    break
                val//= 5
                factor_5 += 1

            u2, u5, _, _ = grid[row - 1][col]
            _, _, l2, l5 = grid[row][col - 1]

            return (factor_2 + u2, factor_5 + u5, factor_2 + l2, factor_5 + l5)
        
        def countZeros(r: int,c: int)-> int:
            up2   ,up5    = grid[r][c][0],grid[r][c][1]
            down2 ,down5  = grid[m-1][c][0]-grid[r-1][c][0],grid[m-1][c][1]-grid[r-1][c][1]
            
            left2 ,left5  = grid[r][c-1][2],grid[r][c-1][3]
            right2,right5 = grid[r][n-1][2]-grid[r][c][2],grid[r][n-1][3]-grid[r][c][3] 

            return max(min(up2+left2 ,up5+left5 ), min(down2+left2 ,down5+left5 ),
                       min(up2+right2,up5+right5), min(down2+right2,down5+right5))

        for r in range(1,m):
            for c in range(1,n):grid[r][c] = prefix_sum(r,c)
        
        return max(countZeros(r,c) for c in range(1,n) for r in range(1,m))