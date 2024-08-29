from collections import defaultdict

class Solution:
    def betterCompression(self, compressed: str) -> str:
        count_dic = defaultdict(int)

        curr_count = 0
        curr_char = ''
        
        for ch in compressed:
            if ch.isalpha():
                if curr_char:
                    count_dic[curr_char] += curr_count
                curr_char = ch
                curr_count = 0
            else:  # ch.isnumeric()
                curr_count = curr_count * 10 + int(ch)
        
        # Add the last character and its count
        if curr_char:
            count_dic[curr_char] += curr_count

        # Build the sorted result
        result = ''.join(f'{char}{count_dic[char]}' for char in sorted(count_dic))
        
        return result
