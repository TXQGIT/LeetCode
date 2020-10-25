package leetcode.graph;

import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class P797_AllPathsFromSource2Target {

    public List<Integer> deepCopy(List<Integer> src){
        try {
            ByteArrayOutputStream byteOut = new ByteArrayOutputStream();
            ObjectOutputStream out = new ObjectOutputStream(byteOut);
            out.writeObject(src);

            ByteArrayInputStream byteIn = new ByteArrayInputStream(byteOut.toByteArray());
            ObjectInputStream in = new ObjectInputStream(byteIn);
            List<Integer> dest = (List<Integer>) in.readObject();
            return dest;
        }catch (Exception e){
            return src;
        }
    }

    public void dfs(int[][] graph, int n, List<List<Integer>> paths, List<Integer> path, boolean[] visited, int node){
        if(path.get(path.size()-1)==n-1){
            paths.add(deepCopy(path));
            return;
        }
        for(int i=0; i<graph[node].length; i++){
            int adjNode = graph[node][i];
            if(!visited[adjNode]){
                path.add(adjNode);
                visited[adjNode] = true;
                dfs(graph, n, paths, path, visited, adjNode);
                visited[adjNode] = false;
                path.remove(path.size()-1);
            }
        }
    }

    public List<List<Integer>> allPathsSourceTarget(int[][] graph) {
        int n = graph.length;
        List<List<Integer>> paths = new ArrayList<List<Integer>>();
        boolean[] visited = new boolean[n];
        List<Integer> path = new ArrayList<>();
        path.add(0);
        visited[0] = true;
        dfs(graph, n, paths, path, visited, 0);
        return paths;
    }

    public static void main(String[] args) {
        P797_AllPathsFromSource2Target solution = new P797_AllPathsFromSource2Target();
        int[][] graph = {{4,3,1},{3,2,4},{3},{4},{}};
        List<List<Integer>> paths = solution.allPathsSourceTarget(graph);
    }
}
