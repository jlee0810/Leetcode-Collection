#include <stack>

class Solution {
public:
    bool isValid(string s) {
        stack<char> seen;

        for (auto c : s) {
            if (c == ')') {
                if (seen.size() == 0 || seen.top() != '(') {
                    return false;
                }
                seen.pop();
            } else if (c == '}') {
                if (seen.size() == 0 || seen.top() != '{') {
                    return false;
                }
                seen.pop();
            } else if (c == ']') {
                if (seen.size() == 0 || seen.top() != '[') {
                    return false;
                }
                seen.pop();
            } else {
                seen.push(c);
            }
        }

        return seen.size() == 0;
    }
};