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
        auto cmp = [](pair<int, ListNode*>a, pair<int, ListNode*>b) {
            return a.first > b.first;
        };

        priority_queue<pair<int, ListNode*>, vector<pair<int, ListNode*>>, decltype(cmp)> min_heap(cmp);

        for (auto lst : lists) {
            if (lst) {
                min_heap.push({lst->val, lst});
            }
        }

        ListNode* dummy = new ListNode();
        ListNode* curr = dummy;

        while (!min_heap.empty()) {
            int val = min_heap.top().first;
            ListNode* node = min_heap.top().second;

            min_heap.pop();

            curr -> next = node;
            curr = curr->next; 

            if (node -> next) {
                min_heap.push(make_pair(node->next->val, node->next));
            } 
        }

        return dummy->next;


    }
};