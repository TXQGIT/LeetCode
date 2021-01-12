package leetcode.sword2offer;

import java.util.ArrayList;
import java.util.List;

public class P49 {
    public int nthUglyNumber(int n) {
        // 从第一个丑数开始查找
        // 定义三个指针: p2, p3, p5分别指向生成下一个丑数时, 该丑数应该是p2,p3,p5所指的数分别乘以2,3,5中的最小值
        List<Integer> ugluList = new ArrayList<>();
        ugluList.add(1);
        int p2 = 0;
        int p3 = 0;
        int p5 = 0;
        int count = 1;
        while (count<n) {
            int p2Value = ugluList.get(p2)*2;
            int p3Value = ugluList.get(p3)*3;
            int p5Value = ugluList.get(p5)*5;
            int nextValue = Math.min(p2Value, Math.min(p3Value, p5Value));
            if (nextValue==p2Value) {
                p2 += 1;
            } else if (nextValue==p3Value) {
                p3 += 1;
            } else {
                p5 += 1;
            }
            if (nextValue==ugluList.get(count-1)){
                continue;
            }
            ugluList.add(nextValue);
            count += 1;
        }
        return ugluList.get(n-1);
    }

    public static void main(String[] args) {
        P49 solution = new P49();
        System.out.println(solution.nthUglyNumber(11));
    }
}
