class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        sum_use = sum(chalk)
        remainder = k % sum_use


        for i in range(len(chalk)):
            remainder -= chalk[i]
            if remainder < 0:
                return i
        