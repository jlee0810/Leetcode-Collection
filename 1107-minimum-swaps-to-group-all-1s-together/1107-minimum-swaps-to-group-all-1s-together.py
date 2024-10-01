class Solution:
    def minSwaps(self, data: List[int]) -> int:
        cnt = Counter(data)
        num_ones = cnt[1]

        l, r = 0, num_ones - 1
        curr_ones = data[l : r + 1].count(1)
        min_swap = num_ones - curr_ones

        while r < len(data) - 1:
            if data[l] == 1:
                curr_ones -= 1
            l += 1
            r += 1
            if data[r] == 1:
                curr_ones += 1
            
            min_swap = min(min_swap, num_ones - curr_ones)

        return min_swap
