package leetcode.graph;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class P1129_ShortestPathwithAlternatingColors {

    private List<Set<Integer>> red_graph = new ArrayList<>();

    private List<Set<Integer>> blue_graph = new ArrayList<>();

    public void buildGraph(int n, int[][] red_edges, int[][] blue_edges){

        for(int i=0; i<n; i++){
            red_graph.add(new HashSet<Integer>());
            blue_graph.add(new HashSet<Integer>());
        }
        for(int i=0; i<red_edges.length; i++){
            int from = red_edges[i][0];
            int to = red_edges[i][1];
            red_graph.get(from).add(to);
        }
        for(int i=0; i<blue_edges.length; i++){
            int from = blue_edges[i][0];
            int to = blue_edges[i][1];
            blue_graph.get(from).add(to);
        }
    }

    public int[] shortestAlternatingPaths(int n, int[][] red_edges, int[][] blue_edges) {
        buildGraph(n, red_edges, blue_edges);
        int[][] dist = new int[n][2];
        for(int i=1; i<n; i++){
            dist[i][0] = -1;
            dist[i][1] = -1;
        }
        List<Integer> nowRed = new ArrayList<Integer>();
        List<Integer> nowBlue = new ArrayList<Integer>();
        nowRed.add(0);
        nowBlue.add(0);
        int step = 0;
        while(!nowRed.isEmpty() || !nowBlue.isEmpty()){
            step += 1;
            List<Integer> newRed = new ArrayList<Integer>();
            List<Integer> newBlue = new ArrayList<Integer>();
            //处理当前的红路径
            if(!nowRed.isEmpty()){
                for(int i=0; i<nowRed.size(); i++){
                    for(int adj : blue_graph.get(nowRed.get(i))){
                        if(dist[adj][0]==-1){
                            dist[adj][0] = step;
                            newBlue.add(adj);
                        }
                    }
                }
            }
            //处理当前的蓝路径
            if(!nowBlue.isEmpty()){
                for(int i=0; i<nowBlue.size(); i++){
                    for(int adj : red_graph.get(nowBlue.get(i))){
                        if(dist[adj][1]==-1){
                            dist[adj][1] = step;
                            newRed.add(adj);
                        }
                    }
                }
            }
            nowRed = newRed;
            nowBlue = newBlue;
        }
        int[] ans = new int[n];
        for(int i=0; i<n; i++){
            if(dist[i][0]==-1 && dist[i][1]==-1){
                ans[i] = -1;
            }else if (dist[i][0]==-1 && dist[i][1]!=-1){
                ans[i] = dist[i][1];
            }else if (dist[i][0]!=-1 && dist[i][1]==-1){
                ans[i] = dist[i][0];
            }else{
                ans[i] = Math.min(dist[i][0], dist[i][1]);
            }
        }
        return ans;
    }

    public static void main(String[] args) {
        P1129_ShortestPathwithAlternatingColors solution = new P1129_ShortestPathwithAlternatingColors();
        int n = 3;
        int[][] red_edges = {{0,1},{1,2}};
        int[][] blue_edges = {};
        System.out.println(solution.shortestAlternatingPaths(n, red_edges, blue_edges));
    }
}
