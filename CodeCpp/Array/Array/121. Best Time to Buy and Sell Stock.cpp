#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
	int maxProfit(vector<int>& prices) {
		// DP����
		// ��dp(i)��ʾ��i��������Ʊʱ�ܻ�õ��������
		// dp(i)=max(dp(i-1)+prices(i)-prices(i-1),0);
		// dp(i-1)+prices(i)-prices(i-1)���С��0����ô��ʾ��i�������ļ۸����ǰ����ļ۸�ͣ���ô������ļ۸����õ���i��ģ��Ժ��ܻ�������
		vector<int> dp(prices.size(),0);
		int maxPro = 0;
		for (int i = 1; i < prices.size(); i++){
			dp[i] = max(dp[i - 1] + prices[i] - prices[i - 1], 0);
		}
		for (int i = 0; i < dp.size(); i++){
			if (dp[i]>maxPro)
				maxPro = dp[i];
		}
		return maxPro;
	}
};

int main(){
	vector<int> prices;
	prices = { 2, 6, 4, 7, 1, 5, 7 };
	Solution S;
	int maxPro = S.maxProfit(prices);
	return 0;
}