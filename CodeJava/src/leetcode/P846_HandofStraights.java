package leetcode;

import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Queue;

public class P846_HandofStraights {

    public boolean isNStraightHand(int[] hand, int W) {
        //使用最小堆组织数组元素,java中使用优先级队列
        //令splited表示当前划分, 同时定义临时数组nextRound
        //每次从取堆顶元素，
        //case1:如果堆顶元素和split的最后1个元素连续,则将堆顶元素加入split
        //case2:如果堆顶元素和split的最后1个元素相等,则将堆顶元素取出保存在nextRound
        //case3:否则,无法划分，直接返回false
        int n = hand.length;
        if (W==1) {
            return true;
        }
        if (n%W!=0) {
            return false;
        }
        Queue<Integer> heap = new PriorityQueue<>();
        for (int i=0; i<n; i++) {
            heap.offer(hand[i]);
        }
        List<Integer> splited = new ArrayList<>();
        List<Integer> nextRound = new ArrayList<>();
        splited.add(heap.poll());
        int curSize = 1;
        while (!heap.isEmpty()) {
            Integer curVal = heap.poll();
            if (splited.get(curSize-1) == curVal-1) {
                splited.add(curVal);
                curSize += 1;
            }else if (splited.get(curSize - 1).equals(curVal)) {
                nextRound.add(curVal);
            }else {
                return false;
            }
            if (curSize<n && curSize%W==0) {
                for (Integer v : nextRound) {
                    heap.offer(v);
                }
                nextRound = new ArrayList<>();
                splited.add(heap.poll());
                curSize += 1;
            }
        }
        return curSize==n;
    }

    public static void main(String[] args) {
        int[] hand = {1,2,3,6,2,3,4,7,8};
        int W = 3;
//        int[] hand = {1,1,2,2,3,3};
//        int W = 2;
        P846_HandofStraights solution = new P846_HandofStraights();
        System.out.println(solution.isNStraightHand(hand, W));
    }

}
