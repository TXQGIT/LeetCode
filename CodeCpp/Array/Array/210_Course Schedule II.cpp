#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void make_graph(vector<pair<int, int>>& req, vector<vector<int>>& G_Adj, vector<int>& indegree){
	for (int i = 0; i<req.size(); i++){
		G_Adj[req[i].second].push_back(req[i].first);
		indegree[req[i].first] += 1;
	}
	return;
}

void topo_sort(int numCourses, vector<vector<int>>& G_Adj, vector<int>& indegree, vector<int>& res){
	for (int i = 0; i<numCourses; i++){
		int j = 0;
		for (j = 0; j<numCourses; j++){
			if (indegree[j] == 0)
				break;
		}
		if (j == numCourses){
			res.clear();
			return;
		}
		indegree[j] -= 1;
		res.push_back(j);
		for (int k = 0; k<G_Adj[j].size(); k++)
			indegree[G_Adj[j][k]] -= 1;
	}
	return;
}

vector<int> findOrder(int numCourses, vector<pair<int, int>>& prerequisites) {
	vector<vector<int>> G_Adj(numCourses);
	vector<int> indegree(numCourses, 0);
	make_graph(prerequisites, G_Adj, indegree);
	vector<int> res;
	topo_sort(numCourses, G_Adj, indegree, res);
	return res;
}

int main(){
	vector<pair<int, int>> req;
	req.push_back(make_pair(1, 0));
	req.push_back(make_pair(2, 0));
	req.push_back(make_pair(3, 1));
	req.push_back(make_pair(3, 2));

	int numCourses = 4;

	int n = rand();
	for (int i = 0; i < 10; i++)
		cout << i++ << endl;
	n = '9' - '0';

	vector<int> res;
	res = findOrder(numCourses, req);
	for (int i = 0; i < res.size(); i++)
		cout << res[i] << endl;
	return 0;
}