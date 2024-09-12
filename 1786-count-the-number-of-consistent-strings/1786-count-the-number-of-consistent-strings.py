class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set = set(allowed)

        count = 0
        for word in words:
            word_set = set(word)
            invalid = False
            for c in word_set:
                if c not in allowed_set:
                    invalid = True
                    break
            if not invalid:
                count += 1
        
        return count