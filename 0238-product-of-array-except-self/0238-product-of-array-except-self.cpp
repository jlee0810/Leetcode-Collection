class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int nums_left = 1;
        int nums_right = 1;
        vector<int> result(nums.size(), 1);

        for (int i = 0; i < nums.size(); i++) {
            result[i] *= nums_left;
            nums_left *= nums[i];
        }

        for (int i = nums.size() - 1; i >= 0; i--) {
            result[i] *= nums_right;
            nums_right *= nums[i];
        }

        return result;
    }
};