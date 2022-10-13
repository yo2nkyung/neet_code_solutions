/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 
 
 6 : 4
 8 : 5
 10 : 6
 
 3 : 2
 5 : 3
 */


struct ListNode* middleNode(struct ListNode* head){
    struct ListNode *p1 = head;
    struct ListNode *p2 = head;
    
    if (head == NULL) return NULL;
    else {
        while (p2 != NULL && p2->next !=NULL) {
            p1 = p1->next;
            p2 = p2->next->next;
        }
    }
    return p1;
}