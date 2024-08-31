class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj_list = collections.defaultdict(list)
        for (v1, v2), prob in zip(edges, succProb):
            adj_list[v1].append((v2, prob))
            adj_list[v2].append((v1, prob))
        
        pq = [(-1, start_node)]
        prob = [0 for _ in range(n)]       
        prob[start_node] = 1

        while pq:
            curr_prob, curr_node = heappop(pq)
            curr_prob *= -1

            if curr_prob < prob[curr_node]:
                continue
            
            for neighbor, success_prob in adj_list[curr_node]:
                new_prob = curr_prob * success_prob

                if new_prob > prob[neighbor]:
                    prob[neighbor] = new_prob
                    heapq.heappush(pq, (-new_prob, neighbor))
                    
        return prob[end_node]
