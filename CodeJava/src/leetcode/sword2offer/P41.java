package leetcode.sword2offer;

import java.util.PriorityQueue;
import java.util.Queue;

class MedianFinder {
    // 最大堆存历史数据流中小值的一半
    // 最小堆存历史数据流中小值的一半
    // 总数为奇数时, 最大堆的数据量比最小堆多1个
    private Queue<Integer> minHeap;
    private Queue<Integer> maxHeap;

    /** initialize your data structure here. */
    public MedianFinder() {
        minHeap = new PriorityQueue<>();
        maxHeap = new PriorityQueue<>();
    }

    public void addNum(int num) {
        maxHeap.offer(-1*num);
        Integer popItem = maxHeap.poll();
        minHeap.offer(-1*popItem);
        if ((maxHeap.size()+minHeap.size())%2==1) {
            popItem = minHeap.poll();
            maxHeap.offer(-1*popItem);
        }
    }

    public double findMedian() {
        double ans = 0;
        if ((maxHeap.size()+minHeap.size())%2==1) {
            ans = -1.0 * maxHeap.peek();
        }else {
            ans = (minHeap.peek()+ -1.0*maxHeap.peek())/2;
        }
        return ans;
    }
}

public class P41 {
    public static void main(String[] args) {
        MedianFinder solution = new MedianFinder();
        solution.addNum(1);
        solution.addNum(2);
        System.out.println(solution.findMedian());
        solution.addNum(3);
        System.out.println(solution.findMedian());
    }
}
