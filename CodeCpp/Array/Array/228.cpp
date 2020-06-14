#include <vector>
//#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

class Solution {
public:
	vector<string> summaryRanges(vector<int>& nums) {
		vector<string> result;
		if (nums.size() == 0)
			return result;
		string temp=num2string(nums[0]);
		int count = 1;
		for (int i = 1; i < nums.size(); i++){
			if (nums[i] - nums[i - 1] != 1){
				if (count>1){
					temp = temp + "->" + num2string(nums[i - 1]);
					result.push_back(temp);
				}
				else
					result.push_back(temp);
				temp = num2string(nums[i]);
				count = 1;
			}
			else
				count++;
		}
		if (count>1){
			temp = temp + "->" + num2string(nums[nums.size()-1]);
			result.push_back(temp);
		}
		else
			result.push_back(temp);
		return result;
	}
	string num2string(int num){
		// C++11标准中函数to_string()能实现相同功能
		string numStr;
		if (num == 0){
			numStr.insert(numStr.begin(), '0');
			return numStr;
		}
		int PorN = 1;
		if (num < 0)
			PorN = 0;
		num = abs(num);
		while (num){
			numStr.insert(numStr.begin(), num % 10 + 48);
			num = num / 10;
		}	
		if (!PorN)
			numStr.insert(numStr.begin(), '-');
		return numStr;
	}
};

int main(){
	vector<int> nums;
//	nums = { -1,0, 1, 2, 4, 5, 7, 9,10 };
	nums = { -2147483648, -2147483647, 2147483647 };
	Solution S;
	string s = to_string(-2147483648);
//	string s = S.num2string(-2147483647);
	vector<string> result=S.summaryRanges(nums);
	return 0;
}