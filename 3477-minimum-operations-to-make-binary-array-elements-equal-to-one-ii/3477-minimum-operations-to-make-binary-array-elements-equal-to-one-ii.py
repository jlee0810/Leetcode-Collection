class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count=0
        for i in nums:
            if i==0 and count%2==0:
                count=count+1
            if i==1 and count%2==1:
                count=count+1
        return count
        