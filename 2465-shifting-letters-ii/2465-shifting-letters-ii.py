from typing import List

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        shift_diff = [0] * (n + 1)  # Difference array

        # Apply all shift operations using the difference array
        for shift_op in shifts:
            start, end, direction = shift_op
            if direction == 1:
                # Forward shift (+1)
                shift_diff[start] += 1
                shift_diff[end + 1] -= 1
            else:
                # Backward shift (-1)
                shift_diff[start] -= 1
                shift_diff[end + 1] += 1

        # Compute the prefix sum to get total shift for each character
        total_shift = 0
        shifted_chars = []

        for i in range(n):
            total_shift += shift_diff[i]
            # Normalize the total_shift to be within [0, 25]
            normalized_shift = total_shift % 26
            # Calculate the new character after shifting
            shifted_char = self.shift_char(s[i], normalized_shift)
            shifted_chars.append(shifted_char)

        # Join the list of characters to form the final string
        return ''.join(shifted_chars)
    
    def shift_char(self, c: str, shift: int) -> str:
        original_pos = ord(c) - ord('a')
        new_pos = (original_pos + shift) % 26
        return chr(new_pos + ord('a'))
