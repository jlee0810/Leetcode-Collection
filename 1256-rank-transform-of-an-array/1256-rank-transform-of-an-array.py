class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_arr = sorted(set(arr))
        rank_map = {num: i + 1 for i, num in enumerate(sorted_arr)}
        return [rank_map[num] for num in arr]
