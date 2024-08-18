class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dist = [float('inf') for _ in range(n)]
        adj_list = defaultdict(list)

        for u, v, w in flights:
            adj_list[u].append((v, w))
        
        dist[src] = 0

        stops = 0
        q = deque()
        q.append((src, 0))

        while stops <= k and q:
            for _ in range(len(q)):
                curr_stop, curr_cost = q.popleft()
                for neighbor, cost in adj_list[curr_stop]:
                    new_cost = cost + curr_cost
                    if new_cost > dist[neighbor]:
                        continue
                    dist[neighbor] = new_cost
                    q.append((neighbor, new_cost))
            stops += 1
        
        return dist[dst] if dist[dst] != float('inf') else -1