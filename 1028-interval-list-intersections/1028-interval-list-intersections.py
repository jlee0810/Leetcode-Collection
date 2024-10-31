class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        result = []

        first_list_idx = 0
        second_list_idx = 0

        while (first_list_idx < len(firstList) and second_list_idx < len(secondList)):
            low = max(firstList[first_list_idx][0], secondList[second_list_idx][0])
            high = min(firstList[first_list_idx][1], secondList[second_list_idx][1])

            if low <= high:
                result.append([low, high])

            if firstList[first_list_idx][1] < secondList[second_list_idx][1]:
                first_list_idx += 1
            else:
                second_list_idx += 1

        return result


