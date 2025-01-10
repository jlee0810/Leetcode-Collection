class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        for word in words:
            if self.isPrefix(word, pref):
                count += 1

        return count

    def isPrefix(self, word, pref):
        if len(pref) > len(word):
            return False
        for i in range(len(pref)):
            if word[i] != pref[i]:
                return False

        return True
