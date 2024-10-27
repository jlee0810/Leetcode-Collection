class Solution {
public:
    int jobScheduling(vector<int>& startTime, vector<int>& endTime, vector<int>& profit) {
        vector<tuple<int, int, int>> intervals;
        for (int i = 0; i < startTime.size(); ++i) {
            tuple<int, int, int> job = {startTime[i], endTime[i], profit[i]};
            intervals.push_back(job);
        }
        
        sort(intervals.begin(), intervals.end());

        unordered_map<int, int> cache;

        auto b_search = [&](int curr_end, int start, int end) {
            int result = intervals.size();
            while (start <= end) {
                int mid = start + (end - start) / 2;
                if (get<0>(intervals[mid]) < curr_end) {
                    start = mid + 1;
                } else {
                    result = min(result, mid);
                    end = mid - 1;
                }
            }
            return result;
        };

        function<int(int)> dp = [&](int i) {
            if (i == intervals.size()) return 0;
            if (cache.find(i) != cache.end()) return cache[i];

            int result = dp(i + 1);
            int next_interval = b_search(get<1>(intervals[i]), i + 1, intervals.size() - 1);
            result = max(result, dp(next_interval) + get<2>(intervals[i]));
            cache[i] = result;

            return result;
        };

        return dp(0);
    }
};
