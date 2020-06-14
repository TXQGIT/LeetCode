#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
	int maxProfit(vector<int>& prices) {
		// DP问题
		// 令dp(i)表示第i天卖出股票时能获得的最大收益
		// dp(i)=max(dp(i-1)+prices(i)-prices(i-1),0);
		// dp(i-1)+prices(i)-prices(i-1)如果小于0，那么表示第i天卖出的价格比以前买入的价格低，那么把买入的价格设置到第i天的，以后能获利更多
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