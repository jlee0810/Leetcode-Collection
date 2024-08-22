class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        dp = [i for i in range(n)]

        result = []

        paths = defaultdict(list)

        for start, end in queries:
            dp[end] = min(dp[end], dp[start] + 1)
            paths[end].append(start)

            for i in range(end + 1, len(dp)):
                for path_start in paths[i]:
                    dp[i] = min(dp[i], dp[path_start] + 1)
                dp[i] = min(dp[i], dp[i - 1] + 1)

            result.append(dp[-1])


        return result