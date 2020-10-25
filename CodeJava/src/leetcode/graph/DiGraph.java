package leetcode.graph;

import java.util.ArrayList;

/* 有向图的邻接表表示 */
public class DiGraph {
    // 有向图的邻接表表示.
    // 图的顶点为数字
    private ArrayList<Integer>[] adj;
    // 根据结点数和有向表数组初始化有向图
    public DiGraph(int n, int[][] edges){
        adj = new ArrayList[n];
        for(int i=0; i<n; i++){
            adj[i] = new ArrayList<Integer>();
        }
        for(int i=0; i<edges.length; i++){
            int tail = edges[i][1];
            int head = edges[i][0];
            adj[tail].add(head);
        }
    }
    // 返回结点v的邻接点
    public Iterable<Integer> adj(int v) {
        return adj[v];
    }

    public int V(){
        return this.adj.length;
    }
}
