class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        distinct = len(set(nums))
        n = len(nums)

        count = 0
        left = 0
        right = 0
        counter = Counter()

        while right < n:
            counter[nums[right]] += 1
            while len(counter) == distinct:
                counter[nums[left]] -= 1
                if counter[nums[left]] == 0:
                    del counter[nums[left]]
                left += 1
                count += n - right
            right += 1

        return count