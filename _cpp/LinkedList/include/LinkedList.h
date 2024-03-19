#pragma once

#include "Utils.h"

using namespace mike;

class LinkedList {
public:
    ListNode* reverseList(ListNode* head);
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2);
    bool hasCycle(ListNode *head);
};