class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        cooldown = deque()
        max_heap = []
        count = Counter(tasks)

        for task in count.values():
            heappush(max_heap, -task)
        

        while max_heap or cooldown:
            time += 1
            if max_heap:
                cnt = heappop(max_heap) + 1
                if cnt < 0:
                    cooldown.append([cnt, time + n])
            if cooldown and cooldown[0][1] <= time:
                heappush(max_heap, cooldown.popleft()[0])
        return time