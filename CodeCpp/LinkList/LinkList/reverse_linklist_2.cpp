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

ListNode *reverseBetween(ListNode *head, int m, int n) {
	ListNode *dummy = new ListNode(0);
	dummy->next = head;
	ListNode *Node_Before_m = dummy;
	for(int i=1;i<m;i++){
		Node_Before_m = Node_Before_m->next;
	}
	ListNode *Node_m = Node_Before_m->next;

	ListNode *reversedHead = NULL;
	ListNode *curNode = Node_m;
	ListNode *preNode = NULL;
	ListNode *nextNode = NULL;
	for(int i=m;i<=n;i++){
		nextNode = curNode->next;
		if (i == n)
			reversedHead = curNode;
		curNode->next = preNode;
		preNode = curNode;
		curNode = nextNode;
	}
	Node_Before_m->next = reversedHead;
	Node_m->next = nextNode;
	return dummy->next;
}

int main(){
	int n = 5;
	int mid = ceil(5 / 2.0);
	int init_arr[] = { 1, 2, 3, 4, 5 };
	vector<int> arr(init_arr, init_arr + 5);
	ListNode *head = createLinkListFromArray(arr);
	printLinkList(head);
	head = reverseBetween(head,1,5);
	printLinkList(head);
	return 0;
}