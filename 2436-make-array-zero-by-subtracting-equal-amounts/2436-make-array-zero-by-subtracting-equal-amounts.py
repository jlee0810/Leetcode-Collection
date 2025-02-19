class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        distinct_positives = {num for num in nums if num > 0}
        return len(distinct_positives)
