#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

//* Definition for a binary tree node.
 struct TreeNode {
     int val;
     TreeNode *left;
     TreeNode *right;
     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 };

class Solution {
public:
/*	TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
		if (inorder.size() <= 0)
			return NULL;
		TreeNode *root = new TreeNode(0);
		int RootVal = *(postorder.end() - 1);
		root->val = RootVal;
		int rootIdx = find_value(inorder, RootVal);

		vector<int> leftIn(inorder.begin(), inorder.begin() + rootIdx);
		vector<int> leftPost(postorder.begin(), postorder.begin() + rootIdx);
		root->left = buildTree(leftIn, leftPost);

		vector<int> rightIn(inorder.begin() + rootIdx + 1, inorder.end());		
		vector<int> rightPost(postorder.begin() + rootIdx, postorder.end()-1);
		root->right = buildTree(rightIn, rightPost);
		return root;
	}*/
	TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
		return BuildTreePI(inorder, 0, inorder.size() - 1, postorder, 0, postorder.size() - 1);
	}
	TreeNode* BuildTreePI(vector<int>& inorder, int in_s, int in_e, vector<int>& postorder, int post_s, int post_e) {
		if (post_s>post_e)
			return NULL;
		TreeNode *root = new TreeNode(0);
		int RootVal = postorder[post_e];
		root->val = RootVal;
		int rootIdx = find_value(inorder, RootVal);

		root->left  = BuildTreePI(inorder, in_s, rootIdx - 1, postorder, post_s, post_s - in_s + rootIdx - 1); //***** 

		root->right = BuildTreePI(inorder, rootIdx + 1, in_e, postorder, post_e - in_e + rootIdx, post_e - 1); //*****

		return root;
	}
	int find_value(vector<int> &nums, int num_find){
		for (int i = 0; i < nums.size(); i++){
			if (nums[i] == num_find)
				return i;
		}
		return nums.size();
	}
};


int main(){
	vector<int> inorder, postorder;
	inorder = { 4, 10, 3, 1, 7, 11, 8, 2 };
	postorder = { 4, 1, 3, 10, 11, 8, 2, 7 };
	int num_find = 10;
	Solution S;
	int pos = S.find_value(inorder, num_find);
	TreeNode *Tree = S.buildTree(inorder, postorder);
	return 0;
}