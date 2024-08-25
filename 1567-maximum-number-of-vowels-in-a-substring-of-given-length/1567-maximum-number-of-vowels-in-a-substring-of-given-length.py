class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        n = len(s)
        
        prefix_sum = [0] * (n + 1)
        
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + (1 if s[i] in vowels else 0)
        
        max_vowels = 0
        
        for i in range(k, n + 1):
            max_vowels = max(max_vowels, prefix_sum[i] - prefix_sum[i - k])
        
        return max_vowels
