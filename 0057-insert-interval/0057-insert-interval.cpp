class Solution {
public:
    std::vector<std::vector<int>> insert(std::vector<std::vector<int>>& intervals, std::vector<int>& newInterval) {
        std::vector<std::vector<int>> result;

        for (int i = 0; i < intervals.size(); i++) {
            if (newInterval[0] > intervals[i][1]) {
                result.push_back(intervals[i]);
            }
            else if (newInterval[1] < intervals[i][0]) {
                result.push_back(newInterval);
                result.insert(result.end(), intervals.begin() + i, intervals.end());
                return result;
            }
            else {
                newInterval[0] = std::min(newInterval[0], intervals[i][0]);
                newInterval[1] = std::max(newInterval[1], intervals[i][1]);
            }
        }
        result.push_back(newInterval);
        return result;
    }
};
