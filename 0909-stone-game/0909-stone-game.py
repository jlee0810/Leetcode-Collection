class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = {}

        def dfs(alice, l, r):
            if (alice, l, r) in dp:
                return dp[(alice, l, r)]
            if l == r:
                return piles[l]
            result = 0 if alice else float('inf')

            if alice:
                result= max(dfs(False, l + 1, r) + piles[l], dfs(False, l, r - 1), piles[r])
            else:
                resut = min(dfs(True, l + 1, r), dfs(True, l, r - 1))
            
            dp[(alice, l, r)] = result
            return result
        
        return dfs(True, 0, len(piles) - 1) > sum(piles) / 2