package leetcode.unionfind;

public class P1319_NumberofOperationstoMakeNetworkConnected {
    public int makeConnected(int n, int[][] connections) {
        int edgeCount = connections.length;
        // 如果总边数小于n-1,则一定不能把所有节点都相连
        if (edgeCount<n-1) {
            return -1;
        }
        UnionFind unionFind = new UnionFind(n);
        for (int i=0; i<edgeCount; i++) {
            unionFind.union(connections[i][0], connections[i][1]);
        }
        int islandCount = 0;
        for (int i=0; i<n; i++) {
            if (unionFind.find(i)==i) {
                islandCount++;
            }
        }
        return islandCount-1;
    }

    public static void main(String[] args) {
        P1319_NumberofOperationstoMakeNetworkConnected solution = new P1319_NumberofOperationstoMakeNetworkConnected();
        int n = 6;
        int[][] connections = {{0,1},{0,2},{0,3},{1,2},{1,3}};
        System.out.println(solution.makeConnected(n, connections));
    }
}
