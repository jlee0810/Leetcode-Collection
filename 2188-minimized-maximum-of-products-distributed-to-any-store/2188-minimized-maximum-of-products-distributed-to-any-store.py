class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def verify(size):
            count = 0
            for quantity in quantities:
                count += math.ceil(quantity / size)
            return count <= n

        l, r = 1, max(quantities)

        result = None
        while l <= r:
            mid = (l + r) // 2
            if verify(mid):
                result = mid
                r = mid - 1
            else:
                l = mid + 1

        return result
