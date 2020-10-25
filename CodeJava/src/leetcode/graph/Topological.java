package leetcode.graph;

/* 基于有向图的邻接表完成拓扑排序 */
public class Topological {

    private Iterable<Integer> order;  //顶点的拓扑排序

    public Topological(DiGraph G){
        DirectedCircle circleFinder = new DirectedCircle(G);
        if(!circleFinder.hasCircle()){
            DepthFirstOrder dfs = new DepthFirstOrder(G);
            order = dfs.reversepost();
        }
    }

    public Iterable<Integer> order(){
        return order;
    }

    public boolean isDAG(){
        return order!=null;
    }
}
