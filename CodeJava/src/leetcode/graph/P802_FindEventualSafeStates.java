package leetcode.graph;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class P802_FindEventualSafeStates {

    public void buildReverseGraph(int[][] graph, List<List<Integer>> reverseGraph, List<Integer> reverseInDegree){
        int n = graph.length;
        for(int i=0; i<n; i++){
            reverseGraph.add(new ArrayList<Integer>());
            reverseInDegree.add(0);
        }
        for(int i=0; i<n; i++){
            for(int j=0; j<graph[i].length; j++){
                int node = graph[i][j];
                reverseGraph.get(node).add(i);
                reverseInDegree.set(i, reverseInDegree.get(i)+1);
            }
        }
    }

    public List<Integer> eventualSafeNodes(int[][] graph) {
        // 对反向图进行拓扑排序
        // 首先建入度为0的节点加入结果集, 加上的同时将该节点的边删掉
        // 依次遍历,直到没有入度为0的节点为准
        List<List<Integer>> reverseGraph = new ArrayList<>();
        List<Integer> reverseInDegree = new ArrayList<>();
        buildReverseGraph(graph, reverseGraph, reverseInDegree);
        Queue<Integer> queue = new LinkedList();
        for(int i=0; i<graph.length; i++){
            if(reverseInDegree.get(i)==0){
                queue.offer(i);
            }
        }
        List<Integer> result = new ArrayList<>();
        while(!queue.isEmpty()){
            int node = queue.poll();
            result.add(node);
            for(Integer adj : reverseGraph.get(node)){
                reverseInDegree.set(adj, reverseInDegree.get(adj)-1);
                if(reverseInDegree.get(adj)==0){
                    queue.offer(adj);
                }
            }
            reverseGraph.set(node, new ArrayList<>());
        }
        return result;
    }

    public static void main(String[] args) {
        P802_FindEventualSafeStates solution = new P802_FindEventualSafeStates();
        int[][] graph = {{1,2},{2,3},{5},{0},{5},{},{}};
        System.out.println(solution.eventualSafeNodes(graph));
    }
}
