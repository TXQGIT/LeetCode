#include <vector>
#include <algorithm>
#include <math.h>
using namespace std;

class Solution {
public:
	int maxProduct(vector<int>& nums) {
		if (nums.size() == 0) {
			return 0;
		}
		int maxherepre = nums[0];
		int minherepre = nums[0];
		int maxsofar = nums[0];
		int maxhere, minhere;
		for (int i = 1; i < nums.size(); i++) {
			maxhere = max(max(maxherepre * nums[i], minherepre * nums[i]), nums[i]);
			minhere = min(min(maxherepre * nums[i], minherepre * nums[i]), nums[i]);
			maxsofar = max(maxhere, maxsofar);
			maxherepre = maxhere;
			minherepre = minhere;
		}
		return maxsofar;
	}

	int maxProduct1(vector<int> A){
		// DP(动态规划)解法
		int n = A.size();
		if (n <= 0)
			return 0;
		
		if (n == 1)
			return A[0];
		int max_local = A[0];
		int min_local = A[0];
		
		int global = A[0];
		for (int i = 1; i != n; ++i) {
			int max_copy = max_local;
			max_local = max(max(A[i] * max_local, A[i]), A[i] * min_local);
			min_local = min(min(A[i] * max_copy, A[i]), A[i] * min_local);
			global = max(global, max_local);		
		}
		return global;
	}

	int MaxProduct_DP(vector<int> nums){
		int n = nums.size();
		int MAX = nums[0];
		vector<int> maxP(n, 0);
		vector<int> minP(n, 0);
		maxP[0] = nums[0];
		minP[0] = nums[0];
		for (int i = 1; i < n; i++){
			maxP[i] = max( max(maxP[i-1] * nums[i], nums[i]), minP[i-1] * nums[i]);
			minP[i] = min( min(maxP[i-1] * nums[i], nums[i]), minP[i-1] * nums[i]);
			MAX = max(MAX, maxP[i]);
		}
		return MAX;
	}
};

int main(){
	vector<int> nums;
	nums = { 2, -3, 3, 0, -2, 3 ,2, -1,4};
	Solution S;
	int MaxP=S.MaxProduct_DP(nums);
	return 0;
}
