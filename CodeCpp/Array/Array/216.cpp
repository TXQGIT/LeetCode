#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
	vector<vector<int>> combinationSum3(int k, int n) {
		vector<vector<int>> result;
		vector<int> temp;
		Func(result, k, n, 1, temp);
		return result;
	}
	void Func(vector<vector<int>> &result, int k, int n, int cur, vector<int> &temp){
		if (k == 1){
			if (n >= cur&&n <= 9){
				temp.push_back(n);
				result.push_back(temp);  //如果找到满足条件的向量那么就添加到result
				temp.pop_back();
			}
			return;
		}
		for (int i = cur; i <= 9; i++){
			if (cur > n)
				break;
			temp.push_back(i);  //将当前的数添加到候选向量temp中，
			Func(result, k - 1, n - i, i + 1, temp);  // 对当前添加到向量temp中的i和temp中其他数递归操作，
			                                          // 如果找到满足条件的向量那么就添加到result， 没找到那就仅仅是该条件下没有temp可添加到result中			                                          
			temp.pop_back();    // 无论是否找到满足条件的temp添加到result中，为保证temp能重复利用，需要temp.pop_back();
		}
	}
};

int main(){
	int k = 3, n = 7;
	Solution S;
    vector<vector<int>> result=S.combinationSum3(k, n);
	return 0;
}