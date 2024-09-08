class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        min_times = float('inf')
        worker_times = [0 for _ in range(k)]

        def backtrack(idx):
            nonlocal min_times
            if idx == len(jobs):
                min_times = max(worker_times)
                return
            for worker_id in range(k):
                if worker_id == 0 or worker_times[worker_id-1] != worker_times[worker_id]: 
                    worker_times[worker_id] += jobs[idx]
                    if max(worker_times) < min_times: 
                        backtrack(idx + 1)
                    worker_times[worker_id] -= jobs[idx]
            
        backtrack(0)
        return min_times
