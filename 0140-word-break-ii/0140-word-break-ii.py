class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        result = []

        def backtrack(start_idx, sentence):
            if start_idx == len(s):
                result.append(" ".join(sentence))
                return
            for end_idx in range(start_idx + 1, len(s) + 1):
                word = s[start_idx : end_idx]
                if word in wordDict:
                    sentence.append(word)
                    backtrack(end_idx, sentence)
                    sentence.pop()
            
        backtrack(0, [])

        return result