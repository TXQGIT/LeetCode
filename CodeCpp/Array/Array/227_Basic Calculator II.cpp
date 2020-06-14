#include <iostream>
#include <stack>
#include <algorithm>

using namespace std;


int cal(int a, int b, char op){
	int ans = 0;
	switch (op){
	case '+': ans = a + b; break;
	case '-': ans = a - b; break;
	case '*': ans = a*b; break;
	case '/': ans = a / b; break;
	}
	return ans;
}

int calculate(string s) {
	stack<int> num;
	stack<char> op;
	int n = s.size();
	for (int i = 0; i<n; i++){
		if (isdigit(s[i])){
			int tmp = s[i] - '0';
			while (i<n - 1 && isdigit(s[i + 1])){
				i += 1;
				tmp = 10 * tmp + (s[i] - '0');
			}
			num.push(tmp);
		}
		else if (s[i] == '*' || s[i] == '/'){
			if (op.empty() || op.top() == '-' || op.top() == '+')
				op.push(s[i]);
			else{
				while (!op.empty() && (op.top() == '*' || op.top() == '/')){
					int b = num.top(); num.pop();
					int a = num.top(); num.pop();
					char p = op.top(); op.pop();
					num.push(cal(a, b, p));
				}
				op.push(s[i]);
			}
		}
		else if (s[i] == '+' || s[i] == '-'){
			if (op.empty())
				op.push(s[i]);
			else{
				while (!op.empty()){
					int b = num.top(); num.pop();
					int a = num.top(); num.pop();
					char p = op.top(); op.pop();
					num.push(cal(a, b, p));
				}
				op.push(s[i]);
			}
		}
	}
	while (!op.empty()){
		int b = num.top(); num.pop();
		int a = num.top(); num.pop();
		char p = op.top(); op.pop();
		num.push(cal(a, b, p));
	}
	return num.top();
}


int main(){
	//string s = "3+2*2";
	//string s = " 3+5 / 2 ";
	//string s = "1*2-3/4+5*6-7*8+9/10";
	//string s = "2*3*4";
	string s = "100000000/1/2/3/4/5/6/7/8/9/10";
	int ans = calculate(s);
	std::cout << s.c_str() << '=' << ans << endl;
	return 0;
}