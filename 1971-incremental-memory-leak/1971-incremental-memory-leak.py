class Solution:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        max_heap = []
        heappush(max_heap, (-memory1, 1))
        heappush(max_heap, (-memory2, 2))

        time = 1
        while max_heap:
            curr_memory_avail, curr_memory_num = heappop(max_heap)
            curr_memory_avail += time
            if curr_memory_avail > 0:
                if curr_memory_num == 1:
                    return [time, (curr_memory_avail - time) * -1, max_heap[0][0] * -1]
                else:
                    return [time, max_heap[0][0] * -1, (curr_memory_avail - time) * -1]
            heappush(max_heap, (curr_memory_avail, curr_memory_num))
            time += 1

