#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        '''
        # recursion
        if not head or not head.next:
            return head
        t = self.reverseList(head.next)
        # print(t)
        head.next.next = head
        head.next = None
        # print(t)
        return t
        '''
        # iterative
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev
# @lc code=end

