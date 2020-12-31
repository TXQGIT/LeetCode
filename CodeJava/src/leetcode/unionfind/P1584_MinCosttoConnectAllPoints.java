package leetcode.unionfind;

import java.util.PriorityQueue;
import java.util.Queue;

public class P1584_MinCosttoConnectAllPoints {
    public int minCostConnectPoints(int[][] points) {
        // 每对节点都构建1条边，再计算这些边组成的图的最小生成树代价
        Queue<WeightEdge> minHeap = new PriorityQueue<>();
        for (int i=0; i<points.length; i++) {
            for (int j=i+1; j<points.length; j++) {
                int dist = Math.abs(points[i][0]-points[j][0]) + Math.abs(points[i][1]-points[j][1]);
                int[] edge = {i, j, dist};
                minHeap.offer(new WeightEdge(edge));
            }
        }
        int mstCost = 0;
        UnionFind unionFind = new UnionFind(points.length);
        while (!minHeap.isEmpty()) {
            WeightEdge curEdge = minHeap.poll();
            if (unionFind.find(curEdge.u)==unionFind.find(curEdge.v)) {
                continue;
            }
            unionFind.union(curEdge.u, curEdge.v);
            mstCost += curEdge.w;
        }
        return mstCost;
    }
}
