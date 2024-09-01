class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        low, up = lower, upper
        for diff in differences:
            low, up = max(lower, low + diff), min(upper, up + diff)
            if low > upper or up < lower: return 0
    
        return up - low + 1 