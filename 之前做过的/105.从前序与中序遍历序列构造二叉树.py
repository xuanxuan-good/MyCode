#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # recursion 前pre：根左右 中in：左根右
        # terminator
        if len(inorder) == 0:
            return None
        # current logic
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        # drill down
        root.left = self.buildTree(preorder[1: mid+1], inorder[0: mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])  #!!!
        # reverse current state
        return root
# @lc code=end

