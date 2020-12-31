package leetcode.unionfind;

import java.util.ArrayList;
import java.util.List;

public class P1627_GraphConnectivityWithThreshold {
    public List<Boolean> areConnected(int n, int threshold, int[][] queries) {
        UnionFind unionFind = new UnionFind(n+1);
        for (int z=threshold+1; z<=n; z++) {
            for (int p=z, q=z*2; q<=n; p+=z, q+=z) {
                unionFind.union(p, q);
            }
        }
        List<Boolean> connected = new ArrayList<>();
        for (int i=0; i<queries.length; i++) {
            if (unionFind.find(queries[i][0])==unionFind.find(queries[i][1])) {
                connected.add(true);
            }else {
                connected.add(false);
            }
        }
        return connected;
    }

    public static void main(String[] args) {
        P1627_GraphConnectivityWithThreshold solution = new P1627_GraphConnectivityWithThreshold();
        int n = 6;
        int threshold = 2;
        int[][] queries = {{1,4},{2,5},{3,6}};
        System.out.println(solution.areConnected(n, threshold, queries));
    }
}
