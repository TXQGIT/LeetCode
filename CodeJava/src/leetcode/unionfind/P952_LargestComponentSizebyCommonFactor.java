package leetcode.unionfind;

public class P952_LargestComponentSizebyCommonFactor {
    public int largestComponentSize(int[] A) {
        int maxVal = 0;
        for (int v : A) {
            maxVal = Math.max(maxVal, v);
        }
        UnionFind unionFind = new UnionFind(maxVal+1);
        for (int v : A) {
            double upBound = Math.sqrt(v);
            for (int i=2; i<=upBound; i++) {
                if (v%i==0) {
                    unionFind.union(v, i);
                    unionFind.union(v, v/i);
                }
            }
        }
        int[] cnt = new int[maxVal+1];
        int res = 0;
        for (int v : A) {
            int root = unionFind.find(v);
            cnt[v] += 1;
            res = Math.max(res, cnt[v]);
        }
        return res;
    }
}
