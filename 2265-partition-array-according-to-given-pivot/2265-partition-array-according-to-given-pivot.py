class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less_than, more_than = [], []
        same_count = 0

        for num in nums:
            if num < pivot:
                less_than.append(num)
            if num == pivot:
                same_count += 1
            if num > pivot:
                more_than.append(num)

        return less_than + [pivot for _ in range(same_count)] + more_than