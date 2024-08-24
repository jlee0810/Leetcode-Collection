class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1
        current_sum = 0

        output = 0
        for num in nums:
            current_sum += num
            if current_sum - k in prefix_sum:
                output += prefix_sum[current_sum - k]
            prefix_sum[current_sum] += 1

        return output