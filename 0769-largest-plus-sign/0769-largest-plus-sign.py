class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        mines_set = set(tuple(mine) for mine in mines)
        
        up = [[0] * n for _ in range(n)]
        down = [[0] * n for _ in range(n)]
        left = [[0] * n for _ in range(n)]
        right = [[0] * n for _ in range(n)]
        
        for i in range(n):
            for j in range(n):
                if (i, j) not in mines_set:
                    up[i][j] = (up[i-1][j] + 1) if i > 0 else 1
                    left[i][j] = (left[i][j-1] + 1) if j > 0 else 1

        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if (i, j) not in mines_set:
                    down[i][j] = (down[i+1][j] + 1) if i < n-1 else 1
                    right[i][j] = (right[i][j+1] + 1) if j < n-1 else 1

        def can_form_plus_sign(size):
            for i in range(size-1, n-size+1):
                for j in range(size-1, n-size+1):
                    if min(up[i][j], down[i][j], left[i][j], right[i][j]) >= size:
                        return True
            return False

        l, r = 1, n
        max_order = 0

        while l <= r:
            mid = (l + r) // 2
            
            if can_form_plus_sign(mid):
                l = mid + 1
                max_order = mid
            else:
                r = mid - 1

        return max_order