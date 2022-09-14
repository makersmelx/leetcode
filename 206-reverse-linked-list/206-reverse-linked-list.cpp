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
    ListNode* reverseList(ListNode* head) {
        ListNode* itr = head;
        ListNode* prev = nullptr;
        while (itr != nullptr) {
            ListNode *next = itr -> next;
            itr -> next = prev;
            prev = itr;
            itr = next;
        }
        return prev;
    }
};