class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        result = []

        def backtrack(idx, subset):
            if idx == len(nums):
                result.append(subset.copy())
                return
            for bool in [True, False]:
                if bool:
                    subset.append(nums[idx])
                    backtrack(idx + 1, subset)
                    subset.pop()
                else:
                    backtrack(idx + 1, subset)
        backtrack(0, [])

        maxBitWise = 0
        maxCount = 0

        for subset in result:
            currentBitWise = 0
            for val in subset:
                currentBitWise = currentBitWise | val
            if currentBitWise > maxBitWise:
                maxCount = 0
                maxBitWise = currentBitWise
            if currentBitWise == maxBitWise:
                maxCount += 1

        return maxCount