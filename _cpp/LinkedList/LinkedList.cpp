#include "LinkedList.h"

ListNode* LinkedList::reverseList(ListNode* head){
    if (head == nullptr)
        return nullptr;

    ListNode* prev = NULL;
    ListNode* node = head;
    ListNode* next = head->next;
    while (node != NULL){
        //std::cout << node->val << " ";
        next = node->next;
        node->next = prev;
        prev = node;
        node = next;
    }

    return prev;        
}

ListNode* LinkedList::mergeTwoLists(ListNode* list1, ListNode* list2) {
    if (!list1) return list2;
    if (!list2) return list1;
    
    ListNode* res = new ListNode();
    ListNode* ptr = res;
    
    while (list1 || list2){
        
        if(!list1){
            res->next = list2;
            break;
        }else if(!list2){
            res->next = list1;
            break;
        }else{
            if (list1->val <= list2->val){
                res->next = new ListNode(list1->val);
                list1 = list1->next;
            }else{
                res->next = new ListNode(list2->val);
                list2 = list2->next;
            }
        }
        res = res->next;
    }
    
    return ptr->next;
}

bool LinkedList::hasCycle(ListNode *head) {

    /******* USING HASHSET
    std::unordered_set<ListNode*> uset;
    
    ListNode* node = head;
    while(node){
        if (uset.find(node) != uset.end())
            return true;
            
        uset.insert(node);
        node = node->next;
    }
    
    return false; 
    ********/

    ListNode* slow = head;
    ListNode* fast = head;
    
    while(fast and fast->next){
        slow = slow->next;
        fast = fast->next->next;
        if (slow == fast)
            return true;
    }
    
    return false;
}

int main(){
    LinkedList ll;

    /* 1. Given the head of a singly linked list, reverse the list, and return the 
    reversed list. */
    {
        std::cout << "\nReverse List" << std::endl;

        ListNode* head = new ListNode(1, new ListNode(2, new ListNode(3, 
            new ListNode(4, new ListNode(5)))));
        head->print();
        ListNode* res = ll.reverseList(head);
        res->print();
        delete res;
    }

    /* 2. You are given the heads of two sorted linked lists list1 and list2.
    Merge the two lists in a one sorted list. The list should be made by 
    splicing together the nodes of the first two lists.
    Return the head of the merged linked list.
    */
    {
        std::cout << "\nMerge two sorted List" << std::endl;
        ListNode* list1 = new ListNode(1, new ListNode(2, new ListNode(4)));
        ListNode* list2 = new ListNode(1, new ListNode(3, new ListNode(4)));
        list1->print();
        list2->print();
        ListNode* res = ll.mergeTwoLists(list1, list2);
        res->print();
        delete res;
    }

    /* 5. Given head, the head of a linked list, determine if the linked list 
    has a cycle in it.
    There is a cycle in a linked list if there is some node in the list that 
    can be reached again by continuously following the next pointer. 
    Internally, pos is used to denote the index of the node that tail's next 
    pointer is connected to. Note that pos is not passed as a parameter.
    Return true if there is a cycle in the linked list. Otherwise, return false.
    */
    {  
        std::cout << "\nLinked List cycle" << std::endl;
        ListNode* tail = new ListNode(-4);
        ListNode* head = new ListNode(3, new ListNode(2, new ListNode(0, tail)));
        tail->next = head->next;

        std::cout << "has cycle: " << ll.hasCycle(head) << std::endl;
    }
}