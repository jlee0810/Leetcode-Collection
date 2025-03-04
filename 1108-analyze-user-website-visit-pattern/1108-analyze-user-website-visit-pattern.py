class Solution:
    def combination(self, arr, wanted_size):
        result = []

        def backtrack(idx, combo):
            nonlocal result

            if len(combo) == wanted_size:
                result.append(combo.copy())
                return
            if idx >= len(arr):
                return

            combo.append(arr[idx])
            backtrack(idx + 1, combo)
            combo.pop()
            backtrack(idx + 1, combo)

        backtrack(0, [])
        return result

    def mostVisitedPattern(
        self, username: List[str], timestamp: List[int], website: List[str]
    ) -> List[str]:
        users = defaultdict(list)

        for user, time, site in sorted(
            zip(username, timestamp, website), key=lambda x: (x[0], x[1])
        ):
            users[user].append(site)
            
        patterns = Counter()

        for user, history in users.items():
            sset = set()
            for combo in self.combination(history, 3):
                sset.add(tuple(combo))
            for combo in sset:
                patterns[combo] += 1

        max_count = 0
        max_pattern = None
        for pattern, count in patterns.items():
            if count > max_count:
                max_pattern = pattern
                max_count = count
            elif count == max_count:
                if pattern < max_pattern:
                    max_pattern = pattern

        return max_pattern
