class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = defaultdict(list)
        for u, v, w in times:
            adj_list[u].append((v, w))
        
        time = {i : float('inf') for i in range(1, n + 1)}
        pq = [(0, k)]
        time[k] = 0

        while pq:
            curr_time, curr_node = heappop(pq)

            if curr_time > time[curr_node]:
                continue
            for neighbor, time_cost in adj_list[curr_node]:
                new_cost = curr_time + time_cost
                if new_cost < time[neighbor]:
                    time[neighbor] = new_cost
                    heappush(pq, (new_cost, neighbor))

        max_time = max(time.values())
        return max_time if max_time < float('inf') else -1
