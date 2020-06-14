#include <iostream>
#include "LinkListDef.h"

using namespace std;

ListNode *reverseLinkList(ListNode *head){
	ListNode *dummy = new ListNode(0);
	ListNode *nextNode = NULL;
	while (head){
		nextNode = head->next;
		head->next = dummy->next;
		dummy->next = head;
		head = nextNode;
	}
	return dummy->next;
}
ListNode *reverseKGroup(ListNode *head, int k) {
	ListNode *preEnd = NULL;
	ListNode *curHead = NULL;
	ListNode *nextHead = NULL;
	ListNode *curNode = head;
	ListNode *tmp = NULL;
	head = NULL;
	while (curNode){
		curHead = curNode;
		tmp = curHead;
		for (int i = 1; i<k&&curNode; i++){
			curNode = curNode->next;
		}
		if (curNode==NULL){
			if (head == NULL)
				head = curHead;
			if (preEnd != NULL){
				preEnd->next = curHead;
			}
			return head;
		}
		else{
			nextHead = curNode->next;
			curNode->next = NULL;
			curHead = reverseLinkList(curHead);
			if (head == NULL)
				head = curHead;
			if (preEnd != NULL)
				preEnd->next = curHead;
			preEnd = tmp;
			curNode = nextHead;
		}
	}
	return head;
}

int main(){
	int a[] = { 1, 2, 3, 4, 5, 6, 7};
	vector<int> data(a, a + 7);
	ListNode *head = creteLinkListFromAaary(data);
	printLinkList(head);
	head = reverseKGroup(head,8);
	printLinkList(head);
	return 0;
}
