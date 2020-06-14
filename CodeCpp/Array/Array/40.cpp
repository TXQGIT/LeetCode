#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
	vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
		sort(candidates.begin(), candidates.end());
		vector<vector<int>> result;
		vector<int> temp;
		Func2(result, target, 0, candidates, temp);  //递归的思想
		return result;
	}
	void Func2(vector<vector<int>> &result, int n, int curPos, vector<int> &candidates, vector<int> &temp){
		// Func2求解40题
		// curPos很关键，如果在函数中去掉该变量会得到重复的答案。
		if (n <= 0){
			if (n == 0)
				result.push_back(temp);
			return;
		}
		for (int i = curPos; i < candidates.size(); i++){
			if (i>curPos&&candidates[i] == candidates[i - 1]) // ??? very important
				continue;
			temp.push_back(candidates[i]);
			Func2(result, n - candidates[i], i+1, candidates, temp);
			temp.pop_back();
		}
	}
	void Func(vector<vector<int>> &result, int n, int curPos, vector<int> &candidates, vector<int> &temp){
		// Func用于求解39题
		// curPos很关键，如果在函数中去掉该变量会得到重复的答案。
		if (n <= 0){
			if (n == 0)
				result.push_back(temp);
			return;
		}
		for (int i = curPos; i < candidates.size(); i++){
			temp.push_back(candidates[i]);
			Func(result, n - candidates[i], i, candidates, temp);
			temp.pop_back();
		}
	}
};

int main(){
	int n = 8;
	vector<int> candidates;
//	candidates = { 2, 3, 6, 7 };
	candidates = { 10, 1, 2, 1, 7, 6, 1, 5 };
	Solution S;
	vector<vector<int>> result = S.combinationSum2(candidates, n);
	return 0;
}