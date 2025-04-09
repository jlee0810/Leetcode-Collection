class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int result = 0;

        set<int> s_nums;

        for (auto num : nums) {
            s_nums.insert(num);
        }

        for (auto num : s_nums) {
            if (s_nums.find(num - 1) == s_nums.end()) {
                int consec = 1;
                int curr = num;
                while (s_nums.find(curr + 1) != s_nums.end()) {
                    consec += 1;
                    curr += 1;
                }
                result = max(result, consec);
            }
        }
        return result;
    }
};