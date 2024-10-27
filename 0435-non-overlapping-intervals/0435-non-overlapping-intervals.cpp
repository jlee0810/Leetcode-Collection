class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        int min_erase = 0;
        int prev_end = INT_MIN;

        sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[1] < b[1];
        });

        for (const auto interval : intervals) {
            if (interval[0] >= prev_end) {
                prev_end = interval[1];
            }
            else {
                min_erase++;
            }
        }

        return min_erase;
    }
};