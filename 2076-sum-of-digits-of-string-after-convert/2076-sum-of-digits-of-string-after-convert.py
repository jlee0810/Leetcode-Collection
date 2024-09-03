class Solution:
    def getLucky(self, s: str, k: int) -> int:
        initial_sum = ""
        for c in s:
            str_num = str(ord(c) - ord('a') + 1)
            initial_sum += str_num
        
        transform = initial_sum
        for _ in range(k):
            curr_sum = sum(int(c) for c in transform)
            transform = str(curr_sum)
        
        return int(transform)