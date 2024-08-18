class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        idx_dict = defaultdict(list)

        for idx, num in enumerate(nums):
            idx_dict[num].append(idx)

        output = [0] * len(nums)
        
        for indices in idx_dict.values():
            n = len(indices)
            
            prefix_sum = list(accumulate(indices))
            
            for i in range(n):
                left = i * indices[i] - (prefix_sum[i - 1] if i > 0 else 0)
                right = (prefix_sum[-1] - prefix_sum[i]) - (n - i - 1) * indices[i]
                output[indices[i]] = left + right
        
        return output
