class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        count = 0
        
        for i in range(total // cost1 + 1):
            count += (total - cost1 * i) // cost2 + 1
        
        return count