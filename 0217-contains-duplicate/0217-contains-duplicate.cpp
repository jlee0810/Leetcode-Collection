#include <set>
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        set <int> sset;
        for (auto num : nums) {
            if (sset.find(num) != sset.end()) {
                return true;
            }
            sset.insert(num);
        }

        return false;
    }
};