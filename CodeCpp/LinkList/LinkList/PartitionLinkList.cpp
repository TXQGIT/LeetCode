#include <iostream>
#include "LinkListDef.h"

using namespace std;

ListNode *partition(ListNode *head, int x) {
	ListNode *part1 = new ListNode(0);
	ListNode *head1 = part1;
	ListNode *part2 = new ListNode(0);
	ListNode *head2 = part2;
	ListNode *tmp = NULL;
	while (head){
		tmp = head->next;
		head->next = NULL;
		if (head->val<x){
			part1->next = head;
			part1 = part1->next;
		}
		else{
			part2->next = head;
			part2 = part2->next;
		}
		head = tmp;
	}
	part1->next = head2->next;
	return head1->next;
}

int main(){
	int a[] = { 1, 4, 3, 2, 5, 2 };
	vector<int> data(a, a + 6);
	ListNode *head = creteLinkListFromAaary(data);
	printLinkList(head);
	head = partition(head, 3);
	printLinkList(head);
	return 0;
}
