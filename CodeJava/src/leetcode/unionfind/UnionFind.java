package leetcode.unionfind;

public class UnionFind {

    public int[] parent;

    public UnionFind(int n){
        this.parent = new int[n];
        for(int i=0; i<n; i++){
            parent[i] = i;
        }
    }

    public int find(int x){
        if(this.parent[x]!=x){
            this.parent[x] = find(parent[x]);
        }
        return this.parent[x];
    }

    public void union(int x, int y){
        int root_x = find(x);
        int root_y = find(y);
        if(root_x!=root_y){
            this.parent[root_x] = root_y;
        }
    }
}
