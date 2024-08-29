class Solution:
    def minSwaps(self, data: List[int]) -> int:
        numOnes = sum(data)
        l, r = 0, 0

        minSwap = float('inf')
        windowOnes = 0
        
        while r < len(data):
            windowOnes += data[r]

            if r - l + 1 == numOnes:
                currentSwap = numOnes - windowOnes
                minSwap = min(minSwap, currentSwap)
                windowOnes -= data[l]
                l += 1
            r += 1

        if minSwap == float('inf'):
            return 0
        return minSwap
