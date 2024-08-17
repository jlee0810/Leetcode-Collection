class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gain = 0
        current_gain = 0

        ans = 0

        for i in range(len(gas)):
            total_gain += gas[i] - cost[i]
            current_gain += gas[i] - cost[i]

            if current_gain < 0:
                current_gain = 0
                ans = i + 1
            
        return ans if total_gain >=0 else -1
