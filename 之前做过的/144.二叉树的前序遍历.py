#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # 迭代 32ms 96%
        res = []; stack = [root]
        while stack:
            node = stack.pop()
            if node:  #!!!
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return res
        '''
        # 递归 根左右 36ms 87%
        res = []
        def preorder(root: TreeNode, res):
            if not root:
                return []
            res.append(root.val)
            preorder(root.left, res)
            preorder(root.right, res)
            return res
        return preorder(root, res)
        '''
# @lc code=end

