package leetcode.graph;

public class P785_IsGraphBipartite {

    public boolean dfs(int[][] graph, boolean[] color, boolean[] visited, int node){
        visited[node] = true;
        for(int i=0; i<graph[node].length; i++){
            int adjNode = graph[node][i];
            if(!visited[adjNode]){
                color[adjNode] = !color[node];
                if(!dfs(graph, color, visited, adjNode)){
                    return false;
                }
            }else{
                if(color[adjNode]==color[node]){
                    return false;
                }
            }
        }
        return true;
    }

    public boolean isBipartite(int[][] graph) {
        int n = graph.length;
        boolean[] color = new boolean[n];
        boolean[] visited = new boolean[n];
        for(int i=0; i<n; i++){
            if(!visited[i] && !dfs(graph, color, visited, i)){
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        P785_IsGraphBipartite solution = new P785_IsGraphBipartite();
        int[][] graph = {{},{2,4,6},{1,4,8,9},{7,8},{1,2,8,9},{6,9},{1,5,7,8,9},{3,6,9},{2,3,4,6,9},{2,4,5,6,7,8}};
        System.out.println(solution.isBipartite(graph));
    }

}
