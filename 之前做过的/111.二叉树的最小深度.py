#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if (root.left is None and root.right is None):
            return 1
        min_depth = 10**9
        if root.left:
            min_depth = min(min_depth,self.minDepth(root.left))
        if root.right:
            min_depth = min(min_depth,self.minDepth(root.right))
        return 1 + min_depth
# @lc code=end

