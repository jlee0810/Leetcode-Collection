class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        min_heap = []
        result = []

        for idx, group in enumerate(groupSizes):
            heappush(min_heap, (group, idx))

        while min_heap:
            curr_group = []
            for _ in range(min_heap[0][0]):
                curr_group.append(min_heap[0][1])
                heappop(min_heap)
            result.append(curr_group)

        return result
        
