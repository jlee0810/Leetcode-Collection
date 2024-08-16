class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        minNum, maxNum = float("inf"), float("-inf")
        secMin, secMax = float("inf"), float("-inf")
        minIdx, maxIdx = -1, -1

        for i, arr in enumerate(arrays):
            if arr[0] < minNum:
                secMin = minNum
                minNum = arr[0]
                minIdx = i
            elif arr[0] < secMin:
                secMin = arr[0]

            if arr[-1] > maxNum:
                secMax = maxNum
                maxNum = arr[-1]
                maxIdx = i
            elif arr[-1] > secMax:
                secMax = arr[-1]

        if minIdx != maxIdx:
            return maxNum - minNum
        else:
            return max(secMax - minNum, maxNum - secMin)