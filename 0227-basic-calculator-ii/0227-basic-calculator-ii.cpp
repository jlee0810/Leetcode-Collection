class Solution {
public:
    int calculate(string s) {
        stack<int> stck;
        char prev_op = '+';
        int num = 0;

        for (int i = 0; i < s.size(); i++) {
            char c = s[i];

            if (isdigit(c)) {
                num = num * 10 + (c - '0');
            }

            if (!isdigit(c) && c != ' ' || i == s.size() - 1) {
                if (prev_op == '+') {
                    stck.push(num);
                }
                else if (prev_op == '-') {
                    stck.push(-num);
                }
                else if (prev_op == '*') {
                    int top = stck.top();
                    stck.pop();
                    stck.push(top * num);
                }
                else if (prev_op == '/') {
                    int top = stck.top();
                    stck.pop();
                    stck.push(top / num);
                }

                prev_op = c;
                num = 0;
            }
        }
        
        int result = 0;

        while(!stck.empty()) {
            int top = stck.top();
            result += top;
            stck.pop();
        }

        return result;
    }
};