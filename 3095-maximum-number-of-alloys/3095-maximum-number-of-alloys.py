class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:
        max_alloy = 0

        for i in range(k):
            low = 0
            high = 1000000000000000

            while low <= high:
                mid = (low + high) // 2
                
                money = 0
                for j in range(n):
                    req = composition[i][j] * mid
                    req -= stock[j]

                    if req >= 0:
                        money += req * cost[j]

                if money <= budget:
                    max_alloy = max(max_alloy, mid)
                    low = mid + 1
                else:
                    high = mid - 1
        return max_alloy