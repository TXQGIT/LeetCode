#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

class Solution {
public:
	vector<vector<int>> subsetsWithDup(vector<int>& nums) {
		// ˼·���ȶ�nums����Ȼ���������nums������
		// ��ÿ��Ԫ�أ������ǰһ��Ԫ�ز�ͬ����ô��subset��ÿ������ȡ��������ĩβ��Ӹ�Ԫ�غ�����ӵ�subset��
		// �����ǰһ��Ԫ����ͬ����ô��subset��ǰһ��Ԫ����ӵ�����һ��ȡ��������ĩβ��Ӹ�Ԫ�غ�����ӵ�subset�С�
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