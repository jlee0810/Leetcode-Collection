class Solution {
public:
    int findMin(vector<int>& nums) {
        int result = 10000000;
        int l = 0, r = nums.size() - 1;

        while (l <= r) {
            int mid = (l + r) / 2;
            result = min(result, nums[mid]);

            if (nums[mid] > nums[r]) {
                l = mid + 1;
            }
            else {
                r = mid - 1;
            }
        }

        return result;
    }
};