#include <vector>

using namespace std;

class Solution {
public:
	int findMin(vector<int>& nums) {

/*		if (*nums.begin() < *(nums.end() - 1))
			return *nums.begin();
		int Min = *(nums.end() - 1);
		for (int i = nums.size() - 2; i >= 0; i--){
			if (nums[i] < nums[i + 1])
				Min = nums[i];
			else
				break;
		}
		return Min;*/

		int start = 0, end = nums.size() - 1;
		while (start<end){
			if (nums[start]<nums[end])
				return nums[start];
			int mid = (start + end) / 2;
			if (nums[mid] >= nums[start])  //由于mid和start可能相等，为避免出错，所以取大于等于而不是只取大于
				start = mid + 1;
			else
				end = mid;
		}
		return nums[start];

	}
};

int main(){
	vector<int> nums;
	nums = {5,6,7,0,1,2,3,4};
	Solution S;
	int minNum=S.findMin(nums);
	return 0;
}