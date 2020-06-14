#include <iostream>
#include "LinkListDef.h"

using namespace std;

ListNode *deleteDuplicates_R(ListNode *head){
	if (head == NULL || head->next == NULL)
		return head;
	ListNode *curNode = NULL;
	if (head->val == head->next->val){  //链表一开始就有重复结点
		curNode = head->next->next;  //一直找到第一个和头结点不同的结点
		while (curNode != NULL && curNode->val == head->val)
			curNode = curNode->next; //一直找到第一个和头结点不同的结点
		return deleteDuplicates_R(curNode);
	}
	else{
		curNode = head->next; //第二个结点
		head->next = deleteDuplicates_R(curNode); //返回的结果作为第一个结点的next
	}
	return head;
}

ListNode *deleteDuplicates(ListNode *head) {
	if (head == NULL)
		return head;
	ListNode *dummy = new ListNode(0);
	dummy->next = head;
	ListNode *lastNode = dummy;
	while (head->next){
		if (head->val != head->next->val){
			if (lastNode->next == head){
				head = head->next;
				lastNode = lastNode->next;
			}
			else{
				head = head->next;
				lastNode->next = head;
			}
		}
		else{
			head = head->next;
		}
	}
	if (lastNode->next != head)
		lastNode->next = NULL;
	return dummy->next;
}

int main(){
	int a[] = { 1, 1, 2, 3, 3, 4, 5 ,5 };
	vector<int> data(a, a + 8);
	ListNode *head = creteLinkListFromAaary(data);
	printLinkList(head);
	//head = deleteDuplicates(head);
	head = deleteDuplicates_R(head);
	printLinkList(head);
	return 0;
}