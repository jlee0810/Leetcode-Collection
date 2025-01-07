class Solution {
public:
    vector<string> stringMatching(vector<string>& words) {
        set<string> result;
        int n = words.size();
        
        for(int i = 0; i < n; ++i){
            for(int j = 0; j < n; ++j){
                if(i != j && words[i].size() <= words[j].size()){
                    if(isSubstring(words[i], words[j])){
                        result.insert(words[i]);
                        break;
                    }
                }
            }
        }
        
        return vector<string>(result.begin(), result.end());
    }
    
private:
    bool isSubstring(const string& sub, const string& target){
        return target.find(sub) != string::npos;
    }
};
