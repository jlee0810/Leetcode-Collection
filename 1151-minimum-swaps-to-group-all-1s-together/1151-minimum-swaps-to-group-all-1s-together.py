class Solution:
    def minSwaps(self, data: List[int]) -> int:
        countOnes = Counter(data)[1]
        l = r = 0
        
        swapNeeded = 0
        while r < countOnes:
            if data[r] == 0:
                swapNeeded += 1
            r += 1
        
        minSwap = swapNeeded
        
        while r < len(data):
            if data[r] == 0:
                swapNeeded += 1
            if data[l] == 0:
                swapNeeded -= 1
            minSwap = min(minSwap, swapNeeded)
            r += 1
            l += 1
        return minSwap
