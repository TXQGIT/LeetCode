package leetcode.graph;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class P1462_CourseScheduleIV {

    private List<List<Integer>> graph;

    public void buildGraph(int n, int[][] prerequisites){
        graph = new ArrayList<>();
        for (int i=0; i<n; i++){
            graph.add(new ArrayList<>());
        }
        for (int i=0; i<prerequisites.length; i++){
            int tail = prerequisites[i][0];
            int head = prerequisites[i][1];
            graph.get(tail).add(head);
        }
    }

    public boolean bfs(int n, int start, int end){
        Queue<Integer> queue = new LinkedList<>();
        boolean[] visited = new boolean[n];
        queue.offer(start);
        visited[start] = true;
        boolean findFlag = false;
        while (!queue.isEmpty() && !findFlag){
            int node = queue.poll();
            for (int adj : graph.get(node)){
                if(!visited[adj]){
                    visited[adj] = true;
                    queue.offer(adj);
                }
                if(adj==end){
                    findFlag = true;
                    break;
                }
            }
        }
        return findFlag;
    }

    public List<Boolean> checkIfPrerequisite(int n, int[][] prerequisites, int[][] queries) {
        buildGraph(n, prerequisites);
        int querySize = queries.length;
        List<Boolean> result = new ArrayList<>();
        for (int i=0; i<querySize; i++){
            result.add(bfs(n, queries[i][0], queries[i][1]));
        }
        return result;
    }

    public static void main(String[] args) {
        int n = 2;
        int[][] prerequisites = {{1,0}};
        int[][] queries = {{0,1},{1,0}};
        P1462_CourseScheduleIV solution = new P1462_CourseScheduleIV();
        System.out.println(solution.checkIfPrerequisite(n, prerequisites, queries));
    }
}
