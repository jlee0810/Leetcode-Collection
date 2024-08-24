class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        p_less, p_more = 0, 0
        
        for index in range(len(nums)):
            targ = nums[index]
            if targ < pivot:
                if index > p_less:
                    nums.insert(p_less, nums.pop(index))
                p_less += 1
                p_more += 1
            elif targ == pivot:
                if index > p_more:
                    temp = nums.pop(index)
                    nums.insert(p_more, temp)
                p_more += 1

        return nums