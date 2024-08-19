class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_l, row_r = 0, len(matrix) - 1
        while row_l <= row_r:
            mid = (row_l + row_r) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                row = mid
                break
            elif target < matrix[mid][0]:
                row_r = mid - 1
            else:
                row_l = mid + 1
        else:
            return False

        row = (row_l + row_r) // 2
        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                l += 1
            else:
                r -= 1
        return False