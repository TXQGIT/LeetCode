#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

struct ListNode{
	int val;
	ListNode* next;
	ListNode(int x) : val(x), next(NULL) {}
};

ListNode *createLinkListFromArray(vector<int> &arr);
int printLinkList(ListNode *head);
ListNode *insertionSortList(ListNode *head);
int findMinVal(ListNode *head);
ListNode *deleteNode(ListNode **head, int minVal);

ListNode *createLinkListFromArray(vector<int> &arr){
	ListNode *dummy = new ListNode(0);
	ListNode *head = dummy;
	for (int i = 0; i < arr.size(); i++){
		head->next = new ListNode(arr[i]);
		head = head->next;
	}
	return dummy->next;
}

int printLinkList(ListNode *head){
	while (head != NULL){
		cout << head->val << "->";
		head = head->next;
	}
	cout << endl;
	return 0;
}

ListNode *insertionSortList(ListNode *head) {
	ListNode *dummy = new ListNode(0);
	dummy->next = head;
	ListNode *LastSortedNode = dummy;
	ListNode *curNode = dummy->next;
	while (curNode!= NULL){
		int minVal = findMinVal(curNode);
		ListNode *minNode = deleteNode(&curNode, minVal);
		minNode->next = curNode;
		LastSortedNode->next = minNode;
		LastSortedNode = minNode;
	}
	return dummy->next;
}
int findMinVal(ListNode *head){
	int minVal = head->val;
	ListNode *curNode = head;
	while (curNode != NULL){
		if (minVal > curNode->val)
			minVal = curNode->val;
		curNode = curNode->next;
	}
	return minVal;
}
ListNode *deleteNode(ListNode **head, int minVal){
	ListNode *minNode = NULL;
	if ((*head)->val == minVal){
		minNode = *head;
		*head = (*head)->next;
		minNode->next = NULL;
		return minNode;
	}
	ListNode *preNode = *head;
	ListNode *curNode = (*head)->next;
	while (curNode != NULL){
		if (curNode->val == minVal){
			preNode->next = curNode->next;
			curNode->next = NULL;
			return curNode;
		}
		preNode = preNode->next;
		curNode = curNode->next;
	}
	return NULL;
}

int main(){
	int n = 5;
	int mid = ceil(5 / 2.0);
	int init_arr[] = { 5, 4, 3, 2, 1 };
	vector<int> arr(init_arr, init_arr + 5);
	ListNode *head = createLinkListFromArray(arr);
	printLinkList(head);
	head = insertionSortList(head);
	printLinkList(head);
	return 0;
}