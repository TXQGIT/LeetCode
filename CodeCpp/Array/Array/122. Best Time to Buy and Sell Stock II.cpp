#include <vector>
#include <algorithm>
#include <numeric>
using namespace std;

class Solution {
public:
	int maxProfit(vector<int>& prices) {
		//在数列的极小值点买入，在下一个极大值点卖出（包含边界）
		int maxPro = 0;
		vector<int> profit(prices.size(), 0);
		for (int i = 1; i < prices.size(); i++){
			profit[i] = max(profit[i-1] + prices[i] - prices[i - 1], 0);
			if (profit[i] <= profit[i - 1])
				profit[i] = 0;
			else
				profit[i - 1] = 0;
		}
		maxPro = accumulate(profit.begin(), profit.end(), 0);
		return maxPro;
	}
	int maxProfit_another(vector<int>& prices) {
		//在数列的极小值点买入，在下一个极大值点卖出（包含边界）
		int maxPro = 0;
		for (int i = 1; i < prices.size(); i++){
			if (prices[i]>prices[i - 1])
				maxPro += prices[i] - prices[i - 1];
		}
		return maxPro;
	}
};

int main(){
	vector<int> prices;
	prices = { 3, 2, 5, 6, 4, 7, 1, 5, 7 };
	Solution S;
//	int maxPro = S.maxProfit(prices);
	int maxPro = S.maxProfit_another(prices);
	return 0;
}