class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        sum_sticks = sum(matchsticks)
        if sum_sticks % 4 != 0:
            return False
        
        sides = [0 for _ in range(4)]

        matchsticks.sort(reverse = True)

        def backtrack(idx):
            if idx == len(matchsticks):
                return sides[0] == sides[1] == sides[2] == sum_sticks // 4
            
            for i in range(4):
                if sides[i] + matchsticks[idx] <= sum_sticks // 4:
                    sides[i] += matchsticks[idx]
                    if backtrack(idx + 1):
                        return True
                    sides[i] -= matchsticks[idx]
            return False
        return backtrack(0)