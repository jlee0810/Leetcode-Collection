class Solution:
    def countAnagrams(self, s: str) -> int:
        MOD = 10**9 + 7
        words = s.split()
        result = 1
        
        for word in words:
            freq = Counter(word)
            word_len = len(word)
            
            total_permutations = factorial(word_len)
            
            for count in freq.values():
                total_permutations //= factorial(count)
            
            result *= total_permutations
            result %= MOD
        
        return result