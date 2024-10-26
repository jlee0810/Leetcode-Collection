/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        struct Compare {
            bool operator()(const pair<int, ListNode*>& a, const pair<int, ListNode*>& b) {
                return a.first > b.first;
            }
        };

        priority_queue<pair<int, ListNode*>, vector<pair<int, ListNode*>>, Compare> pq;

        for (auto lst : lists) {
            if (lst) {
                pq.push({lst->val, lst});
            }
        }


        ListNode* dummy = new ListNode();
        ListNode* curr = dummy;

        while (!pq.empty()) {
            auto [val, node] = pq.top();
            pq.pop();

            curr -> next = node;
            curr = curr -> next;

            if (node -> next) {
                pq.push({node->next->val, node->next});
            }
        }

        return dummy->next;
        
    }
};