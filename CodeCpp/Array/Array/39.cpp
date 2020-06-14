#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
	vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
		sort(candidates.begin(), candidates.end());
		vector<vector<int>> result;
		vector<int> temp;
		Func(result, target, 0, candidates, temp);  //递归的思想
		return result;
	}
	void Func(vector<vector<int>> &result, int n, int curPos, vector<int> &candidates, vector<int> &temp){
		// curPos很关键，如果在函数中去掉该变量会得到重复的答案。
		if (n < candidates[0]){
			if (n == 0)
				result.push_back(temp);
			return;
		}
		for (int i = curPos; i < candidates.size(); i++){
			temp.push_back(candidates[i]);
			Func(result, n-candidates[i], i, candidates, temp);
			temp.pop_back();
		}
	}
};

int main(){
	int n = 11;
	vector<int> candidates;
//	candidates = { 2, 3, 6, 7 };
	candidates = { 8, 7, 4, 3 };
	Solution S;
	vector<vector<int>> result = S.combinationSum(candidates, n);
	return 0;
}