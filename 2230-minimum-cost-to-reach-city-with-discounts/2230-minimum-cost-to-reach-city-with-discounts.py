class Solution:
    def minimumCost(self, n: int, highways: List[List[int]], discounts: int) -> int:
        adj_list = defaultdict(list)
        for depart, dest, cost in highways:
            adj_list[depart].append((dest, cost))
            adj_list[dest].append((depart, cost))
        
        cost = [[float('inf')] * (discounts + 1) for _ in range(n)]
        cost[0][0] = 0
        pq = [(0, 0, 0)]

        while pq:
            curr_cost, curr_node, discount_used = heappop(pq)

            if curr_cost > cost[curr_node][discount_used]:
                continue

            for neighbor, time_cost in adj_list[curr_node]:
                new_cost = curr_cost + time_cost

                if new_cost < cost[neighbor][discount_used]:
                    cost[neighbor][discount_used] = new_cost
                    heappush(pq, (new_cost, neighbor, discount_used))
                
                if discount_used < discounts:
                    discounted_cost = curr_cost + time_cost // 2
                    if discounted_cost < cost[neighbor][discount_used + 1]:
                        cost[neighbor][discount_used + 1] = discounted_cost
                        heappush(pq, (discounted_cost, neighbor, discount_used + 1))

        min_cost = min(cost[n-1])
        return min_cost if min_cost < float('inf') else -1