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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* tmp_head = new ListNode(0, head);
        ListNode* fast = tmp_head, *slow = tmp_head;
        for (int i = 0; i < n ; i++) {
            fast = fast -> next;
        }
        
        while (fast -> next) {
            slow = slow -> next;
            fast = fast -> next;
        }
        
        ListNode* p = slow -> next;
        slow -> next = p -> next;
        delete p;
        return tmp_head -> next;
    }
};