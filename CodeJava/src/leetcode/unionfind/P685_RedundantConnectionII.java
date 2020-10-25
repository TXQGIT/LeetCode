package leetcode.unionfind;

import java.util.ArrayList;
import java.util.List;

public class P685_RedundantConnectionII {

    public int[] getRemoveEdgeOfCircle(int[][] edges){
        int n = edges.length;
        UnionFind unionFind = new UnionFind(n);
        for(int i=0; i<n; i++){
            if(unionFind.find(edges[i][0]-1) == unionFind.find(edges[i][1]-1)){
                return edges[i];
            }
            unionFind.union(edges[i][0]-1, edges[i][1]-1);
        }
        return new int[2];
    }

    public boolean isTreeAfterRemoveEdge(int[][] edges, int idx){
        int n = edges.length;
        UnionFind unionFind = new UnionFind(n);
        for(int i=0; i<n; i++){
            if(i!=idx){
                if(unionFind.find(edges[i][0]-1) == unionFind.find(edges[i][1]-1)){
                    return false;
                }
                unionFind.union(edges[i][0]-1, edges[i][1]-1);
            }
        }
        return true;
    }

    public int[] findRedundantDirectedConnection(int[][] edges) {
        int n = edges.length;
        // 分两种场景
        // 场景1: 图中存在某个节点的入度为2,那只能从该节点的两条入边中选择删除1条
        // 场景2：图中所有节点的入度都是1（即存在环），通过并查集的方式去掉导致出现环的边
        int[] inDegree = new int[n];
        for(int i=0; i<n; i++){
            inDegree[edges[i][1]-1] += 1;
        }
        // 场景1存在则优先处理
        List<Integer> inEdgeOf2InDegreeVertex = new ArrayList<>();
        for(int i=n-1; i>=0; i--){
            if(inDegree[edges[i][1]-1]==2 && isTreeAfterRemoveEdge(edges, i)){
                return edges[i];
            }
        }
        // 场景1不存在, 则处理场景2
        return getRemoveEdgeOfCircle(edges);
    }

    public static void main(String[] args) {
        P685_RedundantConnectionII solution = new P685_RedundantConnectionII();
        //int[][] edges = {{1,2}, {1,3}, {2,3}};
        int[][] edges = {{2,1},{3,1},{4,2},{1,4}};
        //int[][] edges = {{1,2}, {2,3}, {3,4}, {4,1}, {1,5}};
        int[] edge = solution.findRedundantDirectedConnection(edges);
        System.out.println(edge[0]);
        System.out.println(edge[1]);
    }
}
