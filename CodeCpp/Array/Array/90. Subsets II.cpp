#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

class Solution {
public:
	vector<vector<int>> subsetsWithDup(vector<int>& nums) {
		// 思路：先对nums排序，然后遍历整个nums向量。
		// 对每个元素，如果和前一个元素不同，那么把subset中每个向量取出，在其末尾添加该元素后再添加到subset中
		// 如果和前一个元素相同，那么把subset中前一个元素添加的向量一词取出，在其末尾添加该元素后再添加到subset中。
		vector<vector<int>> subset = { {} };
		int Len_pre = subset.size();
		int pos_s = 0;
		vector<int> temp;
		sort(nums.begin(), nums.end());
		for (int i = 0; i < nums.size(); i++){
			if (i == 0){
				subset.push_back({ nums[i] });
				pos_s = 1;
				continue;
			}
			Len_pre = subset.size();
			if (nums[i] == nums[i - 1]){
				for (int j = pos_s; j < Len_pre; j++){
					temp = subset[j];
					temp.push_back(nums[i]);
					subset.push_back(temp);
				}
			}
			else{
				for (int j = 0; j < Len_pre; j++){
					temp = subset[j];
					temp.push_back(nums[i]);
					subset.push_back(temp);
				}
			}
			pos_s = Len_pre;
		}
		return subset;
	}
};

int main(){
	vector<int> nums;
	nums = { 3, 2, 2, 1 };
	Solution S;
	vector<vector<int>> subset = S.subsetsWithDup(nums);
	return 0;
}