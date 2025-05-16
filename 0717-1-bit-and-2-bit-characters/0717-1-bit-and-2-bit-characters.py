class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        idx = 0
        last_character_idx = 0

        while idx < len(bits):
            last_character_idx = idx

            if bits[idx] == 1:
                idx += 2
            else:
                idx += 1

        if bits[last_character_idx] == 1:
            return False
        else:
            return True
