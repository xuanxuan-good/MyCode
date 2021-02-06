#
# @lc app=leetcode.cn id=222 lang=python3
#
# [222] 完全二叉树的节点个数
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        # 2.利用完全二叉树性质
        if not root:
            return 0
        left = self.getDepth(root.left)
        right = self.getDepth(root.right)
        if left == right:  # 左右子树深度相等，说明左边是满二叉树
            return pow(2, left) + self.countNodes(root.right)
        else:  # 左子树深度大于右子树，右子树是满树
            return pow(2, right) + self.countNodes(root.left)
        

    def getDepth(self, root):
        if not root:
            return 0
        return 1 + self.getDepth(root.left)

        '''
        # 1.直接递归求结点个数
        if not root:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        '''

        '''
        # 二分法 O(logn * logn)
        if not root:
            return 0
        d = self.compute_depth(root)
        if d == 0:
            return 1
        left, right = 1, 2**d-1
        while left <= right:
            mid = (left+right) // 2
            if self.exists(mid, d, root):
                left = mid + 1
            else:
                right = mid - 1
        
        return (2**d-1) + left

    def compute_depth(self, node):
        d = 0
        while node.left:
            node = node.left
            d += 1
        return d

    def exists(self, idx, d, node):
        left, right = 0, 2**d-1
        for i in range(d):
            mid = (left + right) // 2
            if idx <= mid:
                right = mid-1
                node = node.left
            else:
                left = mid+1
                node = node.right
        return node is not None
        '''
# @lc code=end

