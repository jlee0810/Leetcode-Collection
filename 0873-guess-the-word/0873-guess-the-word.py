# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        def filter(guess_word, match_count):
            filtered = []
            for word in words:
                if pair_matches(word, guess_word) == match_count:
                    filtered.append(word)
            
            return filtered

        def pair_matches(w1, w2):
            score = 0
            for c1, c2 in zip(w1, w2):
                if c1 == c2:
                    score += 1
            return score
        
        def best_guess():
            char_count = [[0 for _ in range(26)] for _ in range(6)]

            for word in words:
                for i, c in enumerate(word):
                    char_count[i][ord(c) - ord('a')] += 1
            
            best_choice = ""
            best_count = 0

            for word in words:
                count = 0
                for i, c in enumerate(word):
                    count += char_count[i][ord(c) - ord('a')]
                if count > best_count:
                    best_choice = word
                    best_count = count
            
            return best_choice

        while True:
            guess_word = best_guess()
            score = master.guess(guess_word)

            if score == 6:
                break
            else:
                words = filter(guess_word, score)