class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        count1 = Counter(s1)
        count2 = Counter()

        l = 0
        for r in range(len(s2)):
            count2[s2[r]] += 1
            while count2[s2[r]] > count1[s2[r]]:
                count2[s2[l]] -= 1
                if count2[s2[l]] == 0:
                    del count2[s2[l]]
                l += 1
            if r - l + 1 == len(s1):
                return True
        return False
