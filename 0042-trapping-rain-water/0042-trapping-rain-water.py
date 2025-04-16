class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = 0
        max_right = 0
        total = 0
        l, r = 0, len(height) - 1

        while l < r:
            if height[l] < height[r]:
                if max_left - height[l] > 0:
                    total += max_left - height[l]
                max_left = max(max_left, height[l])

                l += 1
            else:
                if max_right - height[r] > 0:
                    total += max_right - height[r]
                max_right = max(max_right, height[r])

                r -= 1
        return total
