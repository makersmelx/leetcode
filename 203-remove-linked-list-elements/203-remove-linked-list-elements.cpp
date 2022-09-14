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
    ListNode* removeElements(ListNode* head, int val) {
        ListNode* start = new ListNode(0, head);
        ListNode* itr = start;
        while (itr != nullptr) {
            if (itr->next != nullptr && itr->next->val == val) {
                ListNode* p = itr->next;
                itr->next = p->next;
                delete p;
            } else {
                itr = itr->next;
            }
            
        }
        return start->next;
    }
};