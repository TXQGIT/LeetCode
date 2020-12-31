package leetcode.unionfind;

import java.util.Arrays;

public class P1579_KeepGraphFullyTraversable {
    // 思路：
    // 1.分别使用并查集算法来分别计算针对Alice和Bob可使用的边在图中的连通分量是多少。若为1，则图连通；反之图为非连通图, 直接返回 -1
    // 2.在并查集算法中，对于每一条边对应的两个顶点，我们检查这两个顶点是否已经在一个连通分量中，若是，则这条边为冗余边，可以直接去掉
    // 3.由于type为3的边为公共边，我们遍历的时候优先遍历公共边，这样就能保证删除的边数量最多
    private boolean[] used;

    public int findRoot(int[] parent, int idx) {
        if (parent[idx]!=idx) {
            parent[idx] = findRoot(parent, parent[idx]);
        }
        return parent[idx];
    }

    public boolean unionFind(int n, int[][] edges, int excludeType) {
        int[] parent = new int[n+1];
        for (int i=1; i<=n; i++) {
            parent[i] = i;
        }
        // 记录当前的连通分量使用了多少条边
        int cnt = 0;
        for (int i=0; i<edges.length; i++) {
            int[] edge = edges[i];
            if (edge[0]==excludeType) {
                continue;
            }
            int rootA = findRoot(parent, edge[1]);
            int rootB = findRoot(parent, edge[2]);
            if (rootA!=rootB) {
                cnt += 1;
                parent[rootA] = rootB;
                used[i] = true;
            }
            // 如果使用了n-1条边,说明整个图可以构成1个联通分量
            if (cnt==n-1) {
                return true;
            }
        }
        return false;
    }

    public int maxNumEdgesToRemove(int n, int[][] edges) {
        used = new boolean[edges.length];
        // 将edges按type降序排列, 保证type3的公共边先被遍历, 进一步保证删除的边最多.
        Arrays.sort(edges, (a,b)->(Integer.compare(b[0], a[0])));
        if (!unionFind(n, edges, 1)) {
            return -1;
        }
        if (!unionFind(n, edges, 2)) {
            return -1;
        }
        int result = 0;
        for (boolean u : used) {
            // 没有使用的边就是可以删除的表
            result += u ? 0 : 1;
        }
        return result;
    }

    public static void main(String[] args) {
        int n = 4;
        int[][] edges = {{3,1,2},{3,2,3},{1,1,3},{1,2,4},{1,1,2},{2,3,4}};
        P1579_KeepGraphFullyTraversable solution = new P1579_KeepGraphFullyTraversable();
        System.out.println(solution.maxNumEdgesToRemove(n, edges));
    }

}
