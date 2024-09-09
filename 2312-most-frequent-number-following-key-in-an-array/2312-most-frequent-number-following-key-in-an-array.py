class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        max_dic = defaultdict(int)

        for i in range(len(nums) - 1):
            if nums[i] == key:
                max_dic[nums[i + 1]] += 1
        
        max_val, max_count = -1, -1

        for key, val in max_dic.items():
            if val > max_count:
                max_val = key
                max_count = val
            
        return max_val
            