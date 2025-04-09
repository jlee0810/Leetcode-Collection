class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int result = 0;
        set<int> s(nums.begin(), nums.end());

        for (auto num : s) {
            if (s.find(num - 1) == s.end()) {
                int consec = 1;
                int curr = num;
                while (s.find(curr + 1) != s.end()) {
                    consec += 1;
                    curr += 1;
                }
                result = max(result, consec);
            }
        }
        return result;
    }
};