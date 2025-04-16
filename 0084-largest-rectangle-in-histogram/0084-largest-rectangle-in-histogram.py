class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        largest = 0
        mono_stack = []

        for idx, height in enumerate(heights):
            start = idx
            while mono_stack and height < mono_stack[-1][0]:
                prev_height, prev_idx = mono_stack.pop()
                largest = max(largest, (idx - prev_idx) * prev_height)
                start = prev_idx
            mono_stack.append([height, start])

        for height, idx in mono_stack:
            largest = max(largest, (len(heights) - idx) * height)

        return largest