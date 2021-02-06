#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # 2.递归  40ms 70% !!!注意方法的定义
        res = []
        def inorder(root: TreeNode, res):
            if root is None:
                return []
            inorder(root.left, res)
            res.append(root.val)
            inorder(root.right, res)
            return res
        return inorder(root, res)
        '''
        # 1.迭代  40ms 70%
        res, stack = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            node = stack.pop()
            res.append(node.val)
            root = node.right
        '''
# @lc code=end

