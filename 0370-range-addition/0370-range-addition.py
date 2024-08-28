class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        #Brute Force
        # result = [0 for _ in range(length)]
        # for update in updates:
        #     startidx, endidx, updateVal = update[0], update[1], update[2]
        #     for i in range(startidx, endidx + 1):
        #         result[i] += updateVal
        # return result

        result = [0 for _ in range(length)]

        for start, end, update in updates:
            result[start] += update
            if end < length - 1:
                result[end + 1] -= update

        for i in range(length - 1):
            result[i + 1] += result[i]
            
        return result