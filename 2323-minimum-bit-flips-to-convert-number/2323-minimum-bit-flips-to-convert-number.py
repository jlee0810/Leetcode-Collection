class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        start_bits, goal_bits = [], []

        while start > 0:
            start_bits.append(start % 2)
            start = start // 2
        
        while goal > 0:
            goal_bits.append(goal % 2)
            goal = goal // 2

        swap = 0
        i = 0

        while i < min(len(start_bits), len(goal_bits)):
            if start_bits[i] != goal_bits[i]:
                swap += 1
            i += 1
        
        while i < len(start_bits):
            if start_bits[i] != 0:
                swap += 1
            i += 1
        
        while i < len(goal_bits):
            if goal_bits[i] == 1:
                swap += 1
            i += 1

        return swap