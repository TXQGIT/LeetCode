#include <iostream>
#include "LinkListDef.h"

using namespace std;

ListNode *rotateRight(ListNode *head, int k) {
	if (head == NULL)
		return head;
	int n = 1;
	ListNode *curNode = head;
	while (curNode->next){
		n += 1;
		curNode = curNode->next;
	}
	curNode->next = head;

	k = k%n;

	curNode = head;
	for (int i = 1; i<n - k; i++){
		curNode = curNode->next;
	}
	ListNode *newHead = curNode->next;
	curNode->next = NULL;
	return newHead;
}

int main(){
	int a[] = { 1, 1, 2, 3, 3, 4, 5, 5 };
	vector<int> data(a, a + 8);
	ListNode *head = creteLinkListFromAaary(data);
	printLinkList(head);
	head = rotateRight(head, 7);
	printLinkList(head);
	return 0;
}