#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
	int minimumTotal_wrong(vector<vector<int>>& triangle) {
		// ��������һ���ƶ�����һ�е�ʲôλ��
		// ��ĿҪ��ÿ�������ƶ�������һ���е��������֡�
		// ��˸��ӳ�����������
		int LEN = triangle.size();
		vector<int> path;
		for (int i = 0; i < LEN; i++){
			path.push_back(triangle[i][0]);
			for (int j = 1; j < triangle[i].size(); j++){
				path[i] = min(path[i], triangle[i][j]);
			}
		}
		int sum = 0;
		for (int k = 0; k < LEN; k++)
			sum += path[k];
		return sum;
	}
	int minimumTotal(vector<vector<int>>& triangle) {
		for (int i = triangle.size() - 2; i >= 0; i--){
			for (int j = 0; j <= i; j++){
				triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1]);
			}
		}
		return triangle[0][0];
	}
};

int main(){
	vector<vector<int>> triangle;
	triangle = { { -1 }, { 2, 3 }, { 1, -1, -3 }};
//	triangle = { { 2 }, { 3, 4 }, { 6, 5, 7 }, { 4, 1, 8, 3 } };
	Solution S;
	int result=S.minimumTotal(triangle);
	return 0;
}