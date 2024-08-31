class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]

        for key in cnt.keys():
            key_count = cnt[key]
            buckets[key_count].append(key)
        
        output = []
        for i in range(len(buckets) - 1, -1, -1):
            for num in buckets[i]:
                if k > 0:
                    output.append(num)
                    k -= 1
        
        return output