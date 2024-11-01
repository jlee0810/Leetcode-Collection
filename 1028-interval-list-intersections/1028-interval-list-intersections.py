class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        first_idx=  0
        second_idx = 0

        result = []

        while first_idx < len(firstList) and second_idx < len(secondList):
            low = max(firstList[first_idx][0], secondList[second_idx][0])
            high = min(firstList[first_idx][1], secondList[second_idx][1])

            if low <= high:
                result.append([low, high])
            
            if firstList[first_idx][1] < secondList[second_idx][1]:
                first_idx += 1
            else:
                second_idx += 1
        
        return result