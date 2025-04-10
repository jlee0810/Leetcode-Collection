class Solution {
public:
    int trap(vector<int>& height) {
        int total = 0;
        int max_left = 0;
        int max_right = 0;

        int l = 0, r = height.size() - 1;

        while (l < r) {
            if (height[l] < height[r]) {
                if (max_left - height[l] > 0) {
                    total += max_left - height[l];
                }

                max_left = max(max_left, height[l]);
                l += 1;
            } else {
                if (max_right - height[r] > 0) {
                    total += max_right - height[r];
                }

                max_right = max(max_right, height[r]);
                r -= 1;
            }
        }

        return total;
    }
};