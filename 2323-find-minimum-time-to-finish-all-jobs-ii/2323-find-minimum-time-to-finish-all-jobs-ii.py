class Solution:
    def minimumTime(self, jobs: List[int], workers: List[int]) -> int:
        sortedJobs = sorted(jobs)
        sortedWorkers = sorted(workers)


        maxDay = 0
        for i in range(len(sortedJobs)):
            maxDay = max(maxDay, -(sortedJobs[i] // -sortedWorkers[i]))

        return maxDay