#
# @lc app=leetcode.cn id=236 lang=python3
#
# [236] 二叉树的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root in (None, p, q):  #628ms
            return root
        left, right = (self.lowestCommonAncestor(kid, p, q) for kid in (root.left, root.right))
        return root if (left and right) else (left or right)
        '''
        # recursion  84ms
        # terminator
        if root is None:
            return None
        # 如果两个结点，有一个是根节点，那么返回根节点即可
        if root == p or root == q:
            return root
        # 如果都不是，那么递归计算左子树和右子树对应的 公共祖先，用left和right表示已经计算好的
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        # 如果左右都有值，那么返回root
        if left and right:
            return root
        # 如果只有一边有值，那么就返回有值这一边
        if not left:
            return right
        if not right:
            return left
        '''
# @lc code=end

