class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        unordered_map<int, vector<int>> adj_list;
        vector<int> in_degree(numCourses, 0);

        for (const auto& prereq : prerequisites) {
            int course = prereq[0];
            int prerequisite = prereq[1];
            adj_list[prerequisite].push_back(course);
            in_degree[course]++;
        }

        queue<int> q;
        for (int i = 0; i < numCourses; ++i) {
            if (in_degree[i] == 0) {
                q.push(i);
            }
        }

        vector<int> order;
        while (!q.empty()) {
            int current = q.front();
            q.pop();
            order.push_back(current);

            for (int neighbor : adj_list[current]) {
                in_degree[neighbor]--;
                if (in_degree[neighbor] == 0) {
                    q.push(neighbor);
                }
            }
        }

        if (order.size() == numCourses) {
            return order;
        } else {
            return {};
        }
    }
};
