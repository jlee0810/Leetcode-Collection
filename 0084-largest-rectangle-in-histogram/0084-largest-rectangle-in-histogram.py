class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        mono_stack = []
        max_area = 0

        for idx, height in enumerate(heights):
            start = idx
            while mono_stack and mono_stack[-1][0] > height:
                prev_height, prev_idx = mono_stack.pop()
                max_area = max(max_area, (idx - prev_idx) * prev_height)
                start = prev_idx
            mono_stack.append([height, start])

        for remaining_height, remaining_idx in mono_stack:
            max_area = max(max_area, (len(heights) - remaining_idx) * remaining_height)

        return max_area
