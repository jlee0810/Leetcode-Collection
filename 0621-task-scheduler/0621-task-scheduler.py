class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        max_heap = []
        cooldown = deque()
        cnt = Counter(tasks)

        for task in cnt.values():
            heappush(max_heap, -task)
        
        while max_heap or cooldown:
            time += 1
            if max_heap:
                task_left = heappop(max_heap) + 1
                if task_left < 0:
                    cooldown.append([task_left, time + n])
            if cooldown and cooldown[0][1] <= time:
                heappush(max_heap, cooldown.popleft()[0])
        
        return time