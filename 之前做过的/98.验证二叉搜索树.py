#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # iterative
        if not root:
            return True
        stack = []
        inorder = float('-inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if (root.val <= inorder):
                return False
            inorder = root.val
            root = root.right
        return True
        '''
        # recursion
        def helper(root, lower = float('-inf'), upper = float('inf')):
            # terminator
            if not root:
                return True
            # current logic
            if root.val <= lower or root.val >= upper:
                return False
            # drill down
            # reverse
            return helper(root.left, lower, root.val) and helper(root.right, root.val, upper)
        return helper(root)
        '''
# @lc code=end

