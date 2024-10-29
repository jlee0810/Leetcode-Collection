class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());

        vector<vector<int>> result;

        int start = 0 ;

        while (start < nums.size() - 2) {
            int l = start + 1;
            int r = nums.size() - 1;

            while (l < r) {
                int curr_sum = nums[start] + nums[l] + nums[r];

                if (curr_sum == 0){
                    result.push_back({nums[start], nums[l], nums[r]});
                    while (l < nums.size() - 1) {
                        if (nums[l + 1] == nums[l]) {
                            l += 1;
                        }
                        else {
                            break;
                        }
                    }
                    l++;

                    while (r > start + 1) {
                        if (nums[r - 1] == nums[r]) {
                            r -= 1;
                        }
                        else {
                            break;
                        }
                    }
                    r--;
                }
                else if (curr_sum < 0) {
                    l += 1;
                }
                else {
                    r -= 1;
                }
            }

            while (start < nums.size() - 2) {
                if (nums[start] == nums[start + 1]) {
                    start += 1;
                }
                else {
                    break;
                }
            }
            start++;
        }

        return result;
    }
};