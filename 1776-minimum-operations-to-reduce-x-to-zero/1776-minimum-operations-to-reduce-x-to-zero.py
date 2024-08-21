class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        
        if target == 0:
            return len(nums)
        
        curr_sum = 0
        max_len = -1
        left = 0
        
        for right in range(len(nums)):
            curr_sum += nums[right]
            
            while curr_sum > target and left <= right:
                curr_sum -= nums[left]
                left += 1
            
            if curr_sum == target:
                max_len = max(max_len, right - left + 1)
        
        return len(nums) - max_len if max_len != -1 else -1

        # if sum(nums) < x:
        #     return -1
        
        # q = deque()
        # q.append((nums[1:], x - nums[0], 1))
        # q.append((nums[:-1], x - nums[-1], 1))

        # while q:
        #     curr_nums, curr_x, curr_operation = q.popleft()
        #     if curr_x == 0:
        #         return curr_operation
            
        #     for idx_subtract in [0, -1]:
        #         if curr_x - curr_nums[idx_subtract] >= 0:
        #             if idx_subtract == 0:
        #                 q.append((curr_nums[1:], curr_x - curr_nums[0], curr_operation + 1))
        #             else:
        #                 q.append((curr_nums[:-1], curr_x - curr_nums[-1], curr_operation + 1))
        # return -1