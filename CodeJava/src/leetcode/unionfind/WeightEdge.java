package leetcode.unionfind;

public class WeightEdge implements Comparable<WeightEdge> {
    public int u;
    public int v;
    public int w;

    public WeightEdge (int[] edge) {
        this.u = edge[0];
        this.v = edge[1];
        this.w = edge[2];
    }

    @Override
    public int compareTo(WeightEdge that) {
        return this.w-that.w;
    }
}
