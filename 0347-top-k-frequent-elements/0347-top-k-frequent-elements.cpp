class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> cnt;
        vector<vector<int>> buckets(nums.size() + 1);
        
        for (int num : nums) {
            cnt[num]++;
        }

        for (const auto& pair : cnt) {
            buckets[pair.second].push_back(pair.first);
        } 

        vector<int> result;
        for (int i = buckets.size() - 1; i > 0 && k > 0; i--) {
            for (int num: buckets[i]) {
                if  (k > 0) {
                    result.push_back(num);
                    k--;
                }
            }
        }

        return result;
    }
};