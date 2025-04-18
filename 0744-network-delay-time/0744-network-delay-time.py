class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = defaultdict(list)

        for n1, n2, cost in times:
            adj_list[n1].append((n2, cost))

        cost = [float("inf") for _ in range(n + 1)]

        pq = []
        heappush(pq, (0, k))

        while pq:
            curr_cost, curr_node = heappop(pq)
            if curr_cost < cost[curr_node]:
                cost[curr_node] = curr_cost

            for nei, nei_cost in adj_list[curr_node]:
                if curr_cost + nei_cost < cost[nei]:
                    heappush(pq, (curr_cost + nei_cost, nei))

        if max(cost[1:]) == float('inf'):
            return -1
        return max(cost[1:])