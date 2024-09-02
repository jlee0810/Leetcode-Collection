class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        results = []

        def backtrack(current_sentence, start_index):
            nonlocal results
            if start_index == len(s):
                results.append(" ".join(current_sentence))
                return
    
            for end_index in range(start_index + 1, len(s) + 1):
                word = s[start_index:end_index]
                if word in word_set:
                    current_sentence.append(word)
                    backtrack(current_sentence, end_index)
                    current_sentence.pop()

        backtrack([],0)
        return results