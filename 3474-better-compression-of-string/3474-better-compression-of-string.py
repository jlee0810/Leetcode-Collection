class Solution:
    def betterCompression(self, compressed: str) -> str:
        count_dic = defaultdict(int)

        curr_count = 0
        curr_char = None
        for i in range(len(compressed)):
            if compressed[i].isalpha():
                if curr_char is not None:
                    count_dic[curr_char] += curr_count
                curr_count = 0
                curr_char = compressed[i]
            elif compressed[i].isnumeric():
                curr_count = curr_count * 10 + int(compressed[i])
        count_dic[curr_char] += curr_count

        lst = list(count_dic.keys())
        lst.sort()

        result = []
        for c in lst:
            result.append(c)
            result.append(str(count_dic[c]))
        return "".join(result)