class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> s_map;
        unordered_map<char, int> t_map;

        for (auto c : s) {
            s_map[c] += 1;
        }
        for (auto c : t) {
            t_map[c] += 1;
        }

        return s_map == t_map;
    }
};