class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda log: log[1])
        queries = sorted([(q, i) for i, q in enumerate(queries)])

        result = [n] * len(queries)
        active_servers = defaultdict(int)

        l, r = 0, 0

        for query, index in queries:
            while r < len(logs) and logs[r][1] <= query:
                active_servers[logs[r][0]] += 1
                r += 1
            while l < len(logs) and logs[l][1] < query - x:
                active_servers[logs[l][0]] -= 1
                if active_servers[logs[l][0]] == 0:
                    del active_servers[logs[l][0]]
                l += 1

            result[index] = n - len(active_servers)

        return result
