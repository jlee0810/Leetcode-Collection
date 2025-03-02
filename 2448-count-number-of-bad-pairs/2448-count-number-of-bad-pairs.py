class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        count = defaultdict(int)

        bad_pair = 0

        for idx, num in enumerate(nums):
            good_pair = count[nums[idx] - idx]
            count[nums[idx] - idx] += 1
            bad_pair += idx - good_pair
            
        return bad_pair