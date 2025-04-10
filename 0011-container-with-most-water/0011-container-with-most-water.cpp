class Solution {
public:
    int maxArea(vector<int>& height) {
        int l = 0, r = height.size() - 1;
        int max_area = 0;

        while (l < r) {
            int area = (r - l) * min(height[l], height[r]);
            max_area = max(max_area, area);

            if (height[l] < height[r]) {
                l += 1;
            } else {
                r -= 1;
            }
        }

        return max_area;
    }
};