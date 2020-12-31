package leetcode.unionfind;

import com.sun.javafx.geom.Edge;
import org.omg.PortableInterceptor.INACTIVE;

import java.util.*;

public class P1489 {

    public int kruskalMST(int[][] edges, int n, int initIdx, boolean withFlag) {
        UnionFind unionFind = new UnionFind(n);
        Queue<WeightEdge> queue = new PriorityQueue<>();
        int mstCost = 0;
        for (int i=0; i<edges.length; i++) {
            if (i!=initIdx) {
                queue.offer(new WeightEdge(edges[i]));
            }else if (withFlag) {
                unionFind.union(edges[i][0], edges[i][1]);
                mstCost += edges[i][2];
            }
        }
        while (!queue.isEmpty()) {
            WeightEdge curEdge = queue.poll();
            if (unionFind.find(curEdge.u)==unionFind.find(curEdge.v)) {
                continue;
            }
            mstCost += curEdge.w;
            unionFind.union(curEdge.u, curEdge.v);
        }
        // 确保生成了最小生成树
        int mstCnt = 0;
        for (int i=0; i<n; i++) {
            if (unionFind.find(i)==i) {
                mstCnt += 1;
            }
        }
        return mstCnt>1?Integer.MAX_VALUE:mstCost;
    }

    public List<List<Integer>> findCriticalAndPseudoCriticalEdges(int n, int[][] edges) {
        int mstCost = kruskalMST(edges, n, -1, false);
        List<Integer> criticalEdges = new ArrayList<>();
        List<Integer> pseudoCriticalEdges = new ArrayList<>();
        for (int i=0; i<edges.length; i++) {
            int mstCostWithoutCurEdge = kruskalMST(edges, n, i, false);
            if (mstCostWithoutCurEdge>mstCost) {
                criticalEdges.add(i);
                continue;
            }
            int mstCostWithCurEdge = kruskalMST(edges, n, i, true);
            if (mstCostWithCurEdge==mstCost) {
                pseudoCriticalEdges.add(i);
            }
        }
        List<List<Integer>> result = new ArrayList<>();
        result.add(criticalEdges);
        result.add(pseudoCriticalEdges);
        return result;
    }

    public static void main(String[] args) {
//        int n = 5;
//        int[][] edges = {{0,1,1},{1,2,1},{2,3,2},{0,3,2},{0,4,3},{3,4,3},{1,4,6}};
        int n = 6;
        int[][] edges = {{0,1,1},{1,2,1},{0,2,1},{2,3,4},{3,4,2},{3,5,2},{4,5,2}};
        P1489 solution = new P1489();
        List<List<Integer>> ans = solution.findCriticalAndPseudoCriticalEdges(n, edges);
        System.out.println(ans);
    }

}
