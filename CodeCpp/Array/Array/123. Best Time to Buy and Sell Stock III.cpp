#include <vector>
#include <algorithm>
#include <numeric>
using namespace std;

class Solution {
public:
	int maxProfit(vector<int>& prices) {
		// 用两个数组，第一个数组f1[i]用来表示在[0,i]内进行买入卖出的最大收益，
		// 用f2[i]表示在[i,n-1]内进行买入卖出的最大收益。
		// 然后最大收益即为max(f1[i]+f2[i])
		int maxPro = 0;
		vector<int> forward(prices.size(), 0);
		vector<int> backward(prices.size(), 0);
		int minPrice = prices[0];
		for (int i = 1; i < prices.size(); i++){
			minPrice = min(minPrice, prices[i]);
			forward[i] = max(forward[i - 1], prices[i] - minPrice);
		}
		int maxPrice = prices[prices.size() - 1];
		for (int i = prices.size() - 2; i >= 0; i--){
			maxPrice = max(maxPrice, prices[i]);
			backward[i] = max(backward[i+1], maxPrice-prices[i]);
		}
		for (int i = 0; i < prices.size(); i++){
			maxPro = max(maxPro, forward[i] + backward[i]);
		}
		return maxPro;
	}
};

int main(){
	vector<int> prices;
//	prices = { 3, 2, 5, 6, 4, 7, 1, 5, 7 };
	Solution S;
	int maxPro = S.maxProfit(prices);
	return 0;
}