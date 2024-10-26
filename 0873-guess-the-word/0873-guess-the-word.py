# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        def removeInvalidWord():
            filtered = []
            for word in words:
                if pair_matches(guess_word, word) == match:
                    filtered.append(word)
            
            return filteredList

        def pair_matches(a, b):
            return sum(c1 == c2 for c1, c2 in zip(a, b))

        def getMostCommon():
            counts = [[0] * 26 for _ in range(6)]

            for w in words:
                for i, c in enumerate(w):
                    counts[i][ord(c) - ord('a')] += 1

            best_score = 0
            best_word = ''

            for w in words:
                curr_score = 0
                for i, c in enumerate(w):
                    curr_score += counts[i][ord(c) - ord('a')]
                if curr_score > best_score:
                    best_score = curr_score
                    best_word = w
            return best_word


        while words:
            guess_word = getMostCommon()
            match = master.guess(guess_word)
            if match == 6:
                return
            words = removeInvalidWord()