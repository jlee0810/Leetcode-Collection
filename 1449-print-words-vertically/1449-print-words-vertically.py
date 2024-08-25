
class Solution:
    def printVertically(self, s: str) -> List[str]:
        s_list = s.split(" ")

        max_length = max(len(word) for word in s_list)
        
        result = [[" " for _ in range(len(s_list))] for _ in range(max_length)]

        for i in range(len(s_list)):
            for j in range(len(s_list[i])):
                result[j][i] = s_list[i][j]

        for i in range(len(result)):
            result[i] = "".join(result[i]).rstrip()
        
        return result
