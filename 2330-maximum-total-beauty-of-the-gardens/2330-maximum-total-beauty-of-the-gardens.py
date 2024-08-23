class Solution:
    def maximumBeauty(self, flowers: List[int], newFlowers: int, target: int, full: int, partial: int) -> int:
        n = len(flowers)
        flowers.sort()
        initialComplete = sum(flowers[i] >= target for i in range(n))
        incompleteGardens = n - initialComplete

        minIncompleteIndex = -1
        minFlowerLevel = 0

        def maximizeMinFlowers() -> None:
            nonlocal minIncompleteIndex, minFlowerLevel, newFlowers
            if j == 0:
                return
            if minIncompleteIndex == -1:
                minIncompleteIndex = 0
                minFlowerLevel = flowers[0]
            while minIncompleteIndex < j:
                nextFlowerLevel = flowers[minIncompleteIndex + 1] if minIncompleteIndex + 1 < j else target - 1
                maxIncrease = min(nextFlowerLevel - minFlowerLevel, newFlowers // (minIncompleteIndex + 1))
                minFlowerLevel += maxIncrease
                newFlowers -= maxIncrease * (minIncompleteIndex + 1)
                if minFlowerLevel != nextFlowerLevel:
                    break
                minIncompleteIndex += 1

        def addCompleteGarden() -> bool:
            nonlocal j, newFlowers
            if j - 1 < 0 or newFlowers < target - flowers[j - 1]:
                return False
            newFlowers -= target - flowers[j - 1]
            j -= 1
            return True

        def removeCompleteGarden() -> None:
            nonlocal j, newFlowers
            newFlowers += target - flowers[j]
            flowers[j] = flowers[j]
            j += 1

        j = incompleteGardens

        while addCompleteGarden():
            pass

        maximizeMinFlowers()

        maxBeauty = full * (n - j) + partial * minFlowerLevel

        while j < incompleteGardens:
            removeCompleteGarden()
            maximizeMinFlowers()
            maxBeauty = max(maxBeauty, full * (n - j) + partial * minFlowerLevel)

        return maxBeauty