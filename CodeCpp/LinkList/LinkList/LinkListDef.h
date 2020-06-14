#ifndef LINK_LIST_DEF
#define LINK_LIST_DEF


#include <vector>

using namespace std;

//Definition for singly-linked list.
struct ListNode {
	int val;
	ListNode *next;
	ListNode(int x) : val(x), next(NULL) {}
};

ListNode *creteLinkListFromAaary(vector<int> &data);

int *printLinkList(ListNode *head);


#endif