class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def valid(capacity):
            day = 1
            curr_ship = 0
            for weight in weights:
                if curr_ship + weight > capacity:
                    day += 1
                    curr_ship = 0
                curr_ship += weight

                if day > days:
                    return False
            return True

        l, r = max(weights), sum(weights)
        min_capacity = None

        while l <= r:
            mid = (l + r) // 2
            if valid(mid):
                min_capacity = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return min_capacity