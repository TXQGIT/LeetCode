package leetcode.graph;

import javax.xml.soap.Node;
import java.util.*;

class DiGraph399{
    // 图的邻接表
    private HashMap<String, HashMap<String, Double>> adj;
    // 图的初始化
    public DiGraph399(ArrayList<ArrayList<String>> equations, double[] values){
        adj = new HashMap<String, HashMap<String, Double>>();
        for(int i=0; i<equations.size(); i++){
            List<String> equation = equations.get(i);
            String dividend = equation.get(0);
            String divisor = equation.get(1);
            double value = values[i];
            if(!adj.containsKey(dividend))
                adj.put(dividend, new HashMap<String, Double>());
            if(!adj.containsKey(divisor))
                adj.put(divisor, new HashMap<String, Double>());
            adj.get(dividend).put(divisor, value);
            adj.get(divisor).put(dividend, 1.0/value);
        }
    }
    // 返回指定节点的邻接节点
    public HashMap<String, Double> adj(String node){
        return adj.get(node);
    }
    // 判断图中是否含指定节点
    public boolean containNode(String node){
        return adj.containsKey(node);
    }
}

public class EvaluateDivision399 {
    // 存储DFS遍历时已访问了哪些节点
    private HashSet<String> visited;
    // 存储在未找到最终结果前, 当前路径的累积
    private double curResult;
    // DFS遍历求解
    public void dfs(DiGraph399 graph, String node, String end){
        // 将当前节点标记为已访问
        this.visited.add(node);
        for(String v : graph.adj(node).keySet()){
            // 如果目标节点还未被访问 且 邻接节点也没有被访问
            if(!this.visited.contains(end) && !this.visited.contains(v)){
                // 路径累积
                this.curResult = this.curResult * graph.adj(node).get(v);
                dfs(graph, v, end);
                // 如果从目标节点还没有找到, 要从其他节点找, 要将累积回退
                if(!this.visited.contains(end))
                    this.curResult = this.curResult / graph.adj(node).get(v);
            }
        }
    }

    public double[] calcEquation(ArrayList<ArrayList<String>> equations, double[] values, ArrayList<ArrayList<String>> queries) {
        int n = queries.size();
        double[] ans = new double[n];
        DiGraph399 graph = new DiGraph399(equations, values);
        for(int i=0; i<queries.size(); i++){
            List<String> query = queries.get(i);
            String dividend = query.get(0);
            String divisor = query.get(1);
            this.visited = new HashSet<String>();
            this.curResult = 1.0;
            if(graph.containNode(dividend) && graph.containNode(divisor))
                dfs(graph, dividend, divisor);
            if(this.visited.contains(divisor))
                ans[i] = this.curResult;
            else
                ans[i] = -1.0;
        }
        return ans;
    }

    public static void main(String[] args) {
        EvaluateDivision399 solution = new EvaluateDivision399();
        ArrayList<ArrayList<String>> equations = new ArrayList<ArrayList<String>>();
        equations.add(new ArrayList<String>(){{ add("a"); add("b"); }});
        equations.add(new ArrayList<String>(){{ add("b"); add("c"); }});
        double[] values = {2.0, 3.0};
        ArrayList<ArrayList<String>> queries = new ArrayList<ArrayList<String>>();
        queries.add(new ArrayList<String>(){{ add("a"); add("c"); }});
        queries.add(new ArrayList<String>(){{ add("b"); add("a"); }});
        queries.add(new ArrayList<String>(){{ add("a"); add("e"); }});
        queries.add(new ArrayList<String>(){{ add("a"); add("a"); }});
        queries.add(new ArrayList<String>(){{ add("x"); add("x"); }});
        double[] ans = solution.calcEquation(equations, values, queries);
        System.out.println(ans);
    }
}
