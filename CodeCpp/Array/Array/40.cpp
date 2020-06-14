#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
	vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
		sort(candidates.begin(), candidates.end());
		vector<vector<int>> result;
		vector<int> temp;
		Func2(result, target, 0, candidates, temp);  //�ݹ��˼��
		return result;
	}
	void Func2(vector<vector<int>> &result, int n, int curPos, vector<int> &candidates, vector<int> &temp){
		// Func2���40��
		// curPos�ܹؼ�������ں�����ȥ���ñ�����õ��ظ��Ĵ𰸡�
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
		// Func�������39��
		// curPos�ܹؼ�������ں�����ȥ���ñ�����õ��ظ��Ĵ𰸡�
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