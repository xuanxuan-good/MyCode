#
# @lc app=leetcode.cn id=226 lang=python3
#
# [226] 翻转二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # 1.recursion
        # terminator
        if not root:
            return root
        # current logic
        root.left, root.right = root.right, root.left
        # drill down
        self.invertTree(root.left)
        self.invertTree(root.right)
        # reverse current states 
        return root  #!!!
        
        '''
        # BFS iterative
        if not root:
            return None
        queue = [root]
        while queue:
            node = queue.pop()
            temp = node.left
            node.left = node.right
            node.right = temp
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root
        '''
# @lc code=end

