class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        cnt1 = Counter(words1)
        cnt2 = Counter(words2)

        count = 0

        for key in cnt1:
            if cnt1[key] > 1:
                continue
            if key in cnt2:
                if cnt2[key] == 1:
                    count += 1


        return count