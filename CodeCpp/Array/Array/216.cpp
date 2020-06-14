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
				result.push_back(temp);  //����ҵ�����������������ô����ӵ�result
				temp.pop_back();
			}
			return;
		}
		for (int i = cur; i <= 9; i++){
			if (cur > n)
				break;
			temp.push_back(i);  //����ǰ������ӵ���ѡ����temp�У�
			Func(result, k - 1, n - i, i + 1, temp);  // �Ե�ǰ��ӵ�����temp�е�i��temp���������ݹ������
			                                          // ����ҵ�����������������ô����ӵ�result�� û�ҵ��Ǿͽ����Ǹ�������û��temp����ӵ�result��			                                          
			temp.pop_back();    // �����Ƿ��ҵ�����������temp��ӵ�result�У�Ϊ��֤temp���ظ����ã���Ҫtemp.pop_back();
		}
	}
};

int main(){
	int k = 3, n = 7;
	Solution S;
    vector<vector<int>> result=S.combinationSum3(k, n);
	return 0;
}