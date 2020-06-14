#include <iostream>
#include "LinkListDef.h"

using namespace std;

ListNode *swapPairs(ListNode *head) {
	if (head == NULL || head->next == NULL)
		return head;
	ListNode *dummy = new ListNode(0);
	dummy->next = head;
	ListNode *pre = head;
	ListNode *cur = pre->next;
	head = dummy;
	while (pre&&cur){
		//head->pre->cur->
		pre->next = cur->next;
		cur->next = pre;
		head->next = cur;
		//head->cur->pre->
		head = pre;
		pre = pre->next;
		if (pre != NULL)
			cur = pre->next;
		else
			cur = NULL;
	}
	return dummy->next;
}

int main(){
	int a[] = { 1, 2, 3, 4, 5, 6, 7, 8 };
	vector<int> data(a, a + 1);
	ListNode *head = creteLinkListFromAaary(data);
	printLinkList(head);
	head = swapPairs(head);
	printLinkList(head);
	return 0;
}