class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if not matchsticks:
            return False
    
        length = len(matchsticks)
        perimeter = sum(matchsticks)
        possible_side =  perimeter // 4

        if perimeter % 4 != 0:
            return False

        matchsticks.sort(reverse = True)
        sums = [0 for _ in range(4)]
    
        def dfs(index):
            if index == length:
                return sums[0] == sums[1] == sums[2] == possible_side
    
            for i in range(4):
                if sums[i] + matchsticks[index] <= possible_side:
                    sums[i] += matchsticks[index]
                    if dfs(index + 1):
                        return True
                    sums[i] -= matchsticks[index]
            return False        
        return dfs(0) 