class Solution:
    def maxPalindromesAfterOperations(self, words: List[str]) -> int:
        words_len = []
        cnt = defaultdict(int)
        for word in words:
            words_len.append(len(word))
            for c in word:
                cnt[c] += 1
        cnt = list(cnt.values())
        words_len.sort()

        pairs = 0
        for count in cnt:
            pairs += count // 2
        
        result = 0
        for length in words_len:
            required_pairs = length // 2
            pairs -= required_pairs
            result += pairs >= 0

        return result