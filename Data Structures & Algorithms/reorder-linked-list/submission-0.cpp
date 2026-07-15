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
    void reorderList(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = head -> next;

        while(fast and fast->next){
            slow = slow -> next;
            fast = fast -> next -> next;
        }

        ListNode* l2 = slow -> next;
        slow -> next = nullptr;
        ListNode* prev = nullptr;

        while(l2){
            ListNode* temp = l2 -> next;
            l2 -> next = prev;
            prev = l2;
            l2 = temp;
        }  
        ListNode* l1 = head;
        l2 = prev;

        while (l2){ 
            ListNode* temp1 = l1 -> next;
            ListNode* temp2 = l2 -> next;
            l1 -> next = l2;
            l2 -> next = temp1;
            l1 = temp1;
            l2 = temp2;
        }
    }
};
