class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {}

        def dfs(i, buy):
            if i >= len(prices):
                return 0
            if (i, buy) in cache:
                return cache[(i, buy)]
            
            if buy:
                buyOption = dfs(i + 1, False) - prices[i]
                coolDown = dfs(i + 1, True)
                cache[(i, buy)] = max(buyOption, coolDown)
            else:
                sellOption = dfs(i + 2, True) + prices[i]
                coolDown = dfs(i + 1, False)
                cache[(i, buy)] = max(sellOption, coolDown)
            
            return cache[(i, buy)]
        
        return dfs(0, True)
