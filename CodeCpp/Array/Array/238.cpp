#include <vector>
using namespace std;

class Solution {
public:
	vector<int> productExceptSelf(vector<int>& nums) {
		vector<int> result(nums.size(),0);
		int count0 = 0, Pos0 = 0, Product = 1;
		for (int i = 0; i < nums.size(); i++){
			if (nums[i] != 0)
				Product *= nums[i];
			else{
				count0++;
				Pos0 = i;
			}	
		}
		if (count0>1)
			return result;
		else if (count0 == 1){
			result[Pos0] = Product;
			return result;
		}
		for (int i = 0; i < nums.size(); i++){
			result[i] = Product / nums[i];
		}
		return result;
	}
	vector<int> productExceptSelf_better(vector<int>& nums) {
		// without division
		// {              1,       a[0], a[0]*a[1], a[0]*a[1]*a[2], }
		// { a[1]*a[2]*a[3],  a[2]*a[3],      a[3],              1, }
		vector<int> result(nums.size(), 1);
		for (int i = 1; i < nums.size(); i++)
			result[i] = result[i - 1] * nums[i - 1];
		int temp = 1;
		for (int i = nums.size() - 1; i >= 0; i--){
			result[i] *= temp;
			temp *= nums[i];
		}
		return result;
	}
};

int main(){
	vector<int> nums;
	nums = { 1, 2, 3, 4 };
	Solution S;
	vector<int> result=S.productExceptSelf_better(nums);
	return 0;
}