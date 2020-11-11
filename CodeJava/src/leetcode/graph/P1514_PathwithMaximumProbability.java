package leetcode.graph;

import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;

class Pair implements Comparable<Pair> {
    int node;
    double prob;

    public Pair(int node, double prob) {
        this.node = node;
        this.prob = prob;
    }

    public int compareTo(Pair pair2) {
        if (this.prob==pair2.prob) {
            return this.node - pair2.node;
        }else{
            return this.prob - pair2.prob > 0 ? -1 : 1;
        }
    }
}

public class P1514_PathwithMaximumProbability {
    private List<List<Pair>> graph;

    public void buildGraph(int n, int[][] edges, double[] succProb) {
        this.graph = new ArrayList<List<Pair>>();
        for (int i=0; i<n; i++) {
            this.graph.add(new ArrayList<Pair>());
        }
        for (int i=0; i<edges.length; i++){
            int[] e = edges[i];
            this.graph.get(e[0]).add(new Pair(e[1], succProb[i]));
            this.graph.get(e[1]).add(new Pair(e[0], succProb[i]));
        }
    }

    public double[] dijkstra(int n, int start) {
        double[] dist = new double[n];
        PriorityQueue<Pair> queue = new PriorityQueue<Pair>();
        queue.offer(new Pair(start, 1.0));
        dist[start] = 1.0;
        while (!queue.isEmpty()) {
            Pair pair = queue.poll();
            int node = pair.node;
            double prob = pair.prob;
            // 由于59行代码没有处理每个结点的历史dist数据, 这里忽略已不是最短距离的结点
            if (prob<dist[node]) {
                continue;
            }
            for (Pair adj : graph.get(node)) {
                int nextNode = adj.node;
                double nextProb = adj.prob;
                if (dist[nextNode]<dist[node]*nextProb){
                    dist[nextNode] = dist[node]*nextProb;
                    // nextNode的历史dist数据暂不移除
                    queue.offer(new Pair(nextNode, dist[nextNode]));
                }
            }
        }
        return dist;
    }

    public double maxProbability(int n, int[][] edges, double[] succProb, int start, int end) {
        // 通过Dijkstra算法计算start结点到其余节点的距离
        buildGraph(n, edges, succProb);
        double[] dist = dijkstra(n, start);
        return dist[end];
    }

    public static void main(String[] args) {
        P1514_PathwithMaximumProbability solution = new P1514_PathwithMaximumProbability();
        int n = 3;
        int[][] edges = {{0,1},{1,2},{0,2}};
        double[] succProb = {0.5,0.5,0.2};
        int start = 0;
        int end = 2;
        System.out.println(solution.maxProbability(n, edges, succProb, start, end));
    }
}
