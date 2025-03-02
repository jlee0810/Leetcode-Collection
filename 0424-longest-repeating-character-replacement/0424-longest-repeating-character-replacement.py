class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        majority = 0
        char_count = defaultdict(int)
        l = 0
        max_length = 0 

        for r in range(len(s)):
            char_count[s[r]] += 1
            majority = max(majority, char_count[s[r]])

            while r - l + 1 - majority > k:
                char_count[s[l]] -= 1
                l += 1
            max_length = max(max_length, r - l + 1)

        return max_length


