class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:        
        need_to_subtract = sum(nums) % p

        if need_to_subtract == 0:
            return 0
        
        prefix_sum = []
        curr_sum = 0
        for num in nums:
            curr_sum += num
            prefix_sum.append(curr_sum)

        min_len = float('inf')
        remainder_to_index = {0: -1}
        for i, prefix in enumerate(prefix_sum):
            remainder = prefix % p
            remainder_to_index[remainder] = i
            target_remainder = (prefix - need_to_subtract) % p
            if target_remainder in remainder_to_index:
                min_len = min(min_len, i - remainder_to_index[target_remainder])

        return min_len if min_len < len(nums) else -1