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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        if(!list1)
            return list2;
        if(!list2)
            return list1;

        ListNode *temp = new ListNode();
        ListNode *ptr = new ListNode();

        if(list1->val >= list2->val){
            temp = list2;
            list2 = list2->next;
        }
        else{
            temp = list1;
            list1 = list1->next;
        }

        ptr = temp;


        while(list1 != NULL && list2 != NULL){
            if(list1->val >= list2->val){
                ptr->next = list2;
                list2 = list2->next;
            }
            else{
                ptr->next = list1;
                list1 = list1->next;
            }
            ptr = ptr->next;
        }
    if(list1 != NULL)
        ptr->next = list1;
    else
        ptr->next = list2;
        
    return temp;
    }
};