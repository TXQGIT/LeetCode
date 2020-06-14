#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

bool isPalindrome(string s) {
	if (s.size() == 0)
		return true;
	int begin = 0;
	int end = s.size() - 1;
	//isdigit() ×ÖÄ¸´óÐ´Ð¡Ð´
	//isalpha() Êý×Ö
	//isalnum() ×ÖÄ¸´óÐ´Ð¡Ð´+Êý×Ö
	while (!isalnum(s[begin]))
		begin++;
	while (!isalnum(s[end]))
		end--;
	if (begin>end || tolower(s[begin]) != tolower(s[end]))
		return false;
	else
		return isPalindrome(s.substr(begin + 1, max(end - begin-1,0)));
}

int main(){
	//string s = "";
	string s = "A man, a plan, a canal: Panama";
	string::iterator ptr = s.begin();
	while (ptr != s.end())
		cout << *(ptr++);
	bool flag = isPalindrome(s);
	return 0;
}