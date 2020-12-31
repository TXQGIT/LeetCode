package leetcode.sword2offer;

import javax.swing.tree.TreeNode;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;
import java.util.Queue;

public class P33 {
    // 判断postorder数组是不是某个二叉搜索树的后序遍历
    public boolean verifyPostorder(int[] postorder) {
        int n = postorder.length;
        if (n==0) {
            return true;
        }
        int rootVal = postorder[n-1];
        // 取出左侧小于根节点的子数组作为左子树
        int leftIdx = 0;
        while (leftIdx<n) {
            if (postorder[leftIdx]<rootVal) {
                leftIdx += 1;
            }else {
                break;
            }
        }
        int[] left = Arrays.copyOf(postorder, leftIdx);
        // 取剩余区间为右子树(要排除根节点)
        int[] right = new int[n-leftIdx-1];
        for (int i=leftIdx; i<n-1; i++) {
            // 如果剩余区间有小于根节点的值, 说明肯定不是二叉搜素树
            if (postorder[i]<rootVal) {
                return false;
            }
            right[i-leftIdx] = postorder[i];
        }
        return verifyPostorder(left) && verifyPostorder(right);
    }

    public static void main(String[] args) {
//        int[] postOrder = {1,6,3,2,5};
        int[] postOrder = {1,3,2,6,5};
        P33 solution = new P33();
        System.out.println(solution.verifyPostorder(postOrder));
    }
}
