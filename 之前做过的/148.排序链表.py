#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] 排序链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # 快排 超时25/28
        return self.quick_sort(head)
    def quick_sort(self, head):
        if not head or not head.next:
            return head
        dummy = self.partition(head)
        right = self.quick_sort(head.next)  # 分区点右侧的，因为刚开始以第一个元素为分区点，所以right就从head.next开始
        head.next = None  # 看着像是为了下边left，区分出左边界，所以把head.next设置为None
        left = self.quick_sort(dummy)  # 分区点左侧的
        curr = left
        while curr.next:
            curr = curr.next
        curr.next = right
        return left  # 合并后的
    def partition(self, head):
        dummy1 = p = ListNode(-1)
        dummy2 = q = ListNode(-1)
        pivot = head.val  # 第一个元素作为分区
        while head:
            if head.val < pivot:
                p.next = head
                p = p.next
            else:
                q.next = head
                q = q.next
            head = head.next
        p.next = dummy2.next
        q.next = None
        return dummy1.next
# @lc code=end

s = Solution()
s.sortList(ListNode(val = 2, next = ListNode(val = 1, next = ListNode(val = 4, next = None))))