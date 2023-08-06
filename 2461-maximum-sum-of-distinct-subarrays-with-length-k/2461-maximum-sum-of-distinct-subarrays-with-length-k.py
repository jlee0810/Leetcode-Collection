class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        l, r = 0, 0
        maxSum = 0
        currentSum = 0
        counter = defaultdict(int)

        while r < len(nums):
            counter[nums[r]] += 1
            currentSum += nums[r]

            while counter[nums[r]] > 1:
                counter[nums[l]] -= 1
                currentSum -= nums[l]
                if counter[nums[l]] == 0:
                    del counter[nums[l]]
                l += 1
            
            if r - l + 1 == k:
                maxSum = max(maxSum, currentSum)
                counter[nums[l]] -= 1
                currentSum -= nums[l]
                if counter[nums[l]] == 0:
                    del counter[nums[l]]
                l += 1

            r += 1

        return maxSum