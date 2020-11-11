package leetcode.graph;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class P1494_ParallelCoursesII {

    private List<List<Integer>> graph;

    private int[] inDegree;

    public void buildGraph(int n, int[][] edges){
        graph = new ArrayList<>();
        inDegree = new int[n];
        for (int i=0; i<n; i++){
            graph.add(new ArrayList<>());
        }
        for (int i=0; i<edges.length; i++){
            int tail = edges[i][0]-1;
            int head = edges[i][1]-1;
            graph.get(tail).add(head);
            inDegree[head] += 1;
        }
    }

    public int minNumberOfSemesters(int n, int[][] dependencies, int k) {
        buildGraph(n, dependencies);
        Queue<Integer> queue = new LinkedList<>();
        for (int i=0; i<n; i++){
            if (inDegree[i]==0){
                queue.offer(i);
            }
        }
        int cnt = 0;
        while (!queue.isEmpty()){
            // 单次遍历最多取k个节点
            int curSize = queue.size();
            for (int i=0; i<Math.min(curSize, k); i++){
                int node = queue.poll();
                // 遍历每个节点的邻接点
                for (int adj : graph.get(node)){
                    // 拓扑排序不需要用visited标记节点是否已经访问
                    // 邻接点入度减1
                    inDegree[i] -= 1;
                    // 如果节点的入度为0,则加入队列
                    if (inDegree[adj]==0){
                        queue.offer(adj);
                    }
                }
            }
            cnt += 1;
        }
        return cnt;
    }

    public static void main(String[] args) {
//        int n = 4;
//        int[][] dependencies = {{2,1},{3,1},{1,4}};
//        int k = 2;
        int n = 5;
        int[][] dependencies = {{2,1},{3,1},{4,1},{1,5}};
        int k = 2;
        P1494_ParallelCoursesII solution = new P1494_ParallelCoursesII();
        System.out.println(solution.minNumberOfSemesters(n, dependencies, k));
    }
}
