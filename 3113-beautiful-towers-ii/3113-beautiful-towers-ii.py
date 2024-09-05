class Solution:
    def maximumSumOfHeights(self, heights: List[int]) -> int:
        n = len(heights)
        
        def calculate_prefix_sums(heights):
            prefix_sums = [0]
            stack = []
            current_sum = 0
            
            for index in range(n):
                width = 1
                while stack and heights[index] <= heights[stack[-1][0]]:
                    prev_index, prev_width = stack.pop()
                    current_sum -= heights[prev_index] * prev_width
                    width += prev_width
                
                stack.append([index, width])
                current_sum += heights[index] * width
                prefix_sums.append(current_sum)
            
            return prefix_sums
        
        left_prefix_sums = calculate_prefix_sums(heights)
        right_prefix_sums = calculate_prefix_sums(heights[::-1])[::-1]
        
        return max(left_prefix_sums[i] + right_prefix_sums[i] for i in range(n + 1))
