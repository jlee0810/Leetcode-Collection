class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> anagram_dict;

        for (auto& s : strs) {
            string sorted_s = s;
            sort(sorted_s.begin(), sorted_s.end());
            anagram_dict[sorted_s].push_back(s);
        }

        vector<vector<string>> result;

        for (auto& pair : anagram_dict) {
            result.push_back(pair.second);
        }

        return result;
    }
};