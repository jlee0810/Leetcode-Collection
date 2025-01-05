class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        shift_diff = [0] * (n + 1)

        for shift_op in shifts:
            start, end, direction = shift_op
            if direction == 1:
                shift_diff[start] += 1
                shift_diff[end + 1] -= 1
            else:
                shift_diff[start] -= 1
                shift_diff[end + 1] += 1

        total_shift = 0
        shifted_chars = []

        for i in range(n):
            total_shift += shift_diff[i]
            normalized_shift = total_shift % 26
            shifted_char = self.shift_char(s[i], normalized_shift)
            shifted_chars.append(shifted_char)

        return ''.join(shifted_chars)
    
    def shift_char(self, c: str, shift: int) -> str:
        original_pos = ord(c) - ord('a')
        new_pos = (original_pos + shift) % 26
        return chr(new_pos + ord('a'))
