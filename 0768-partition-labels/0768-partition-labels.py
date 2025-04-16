class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        idx_dic = {}

        for i in range(len(s)):
            idx_dic[s[i]] = i

        result = []

        curr_len = 0
        curr_part_max = 0

        for i in range(len(s)):
            char = s[i]
            curr_part_max = max(curr_part_max, idx_dic[char])
            curr_len += 1

            if curr_part_max == i:
                result.append(curr_len)
                curr_len = 0

        return result
