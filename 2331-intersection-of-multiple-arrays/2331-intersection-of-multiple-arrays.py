class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        s = set(nums[0])
        
        for lst in nums[1:]:
            s.intersection_update(set(lst))
        
        return sorted(s)