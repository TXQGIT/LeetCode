#include <iostream>
#include "LinkListDef.h"

using namespace std;


ListNode *creteLinkListFromAaary(vector<int> &data){
	ListNode *head = new ListNode(0);
	ListNode *curNode = head;
	for (int i = 0; i < data.size(); i++){
		ListNode *newNode = new ListNode(data[i]);
		curNode->next = newNode;
		curNode = curNode->next;
	}
	return head->next;
}

int *printLinkList(ListNode *head){
	while (head){
		std::cout << head->val << "->";
		head = head->next;
	}
	std::cout << "NULL" << std::endl;
	return 0;
}