#
# @lc app=leetcode.cn id=1046 lang=python3
#
# [1046] 最后一块石头的重量
#

# @lc code=start
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # 2.优先队列
        heap = [-i for i in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            heapq.heappush(heap, heapq.heappop(heap) - heapq.heappop(heap))
        return -heap[0]

        '''
        '''
        # 3.双指针的想法，类似计数，先建立一个1001大小的桶，因为stones[i]的范围是1-1000
        # bucket桶内装的是：每个重量的石头有多少个。。慢指针定位到桶的最后，之后向前遍历循环
        # 如果慢指针对应的桶内石头个数为奇数，才有可能剩下一个没有被完全粉碎的石头：
        #     因此每次看到这样的位置，就把快指针定位到该位置的前边，
        #     找到不为空的快慢指针对应的位置，然后bucket[fast]--；bucket[slow - fast]++
        # 最后要么slow遍历到0，要么fast遍历到0，则终止返回slow，即剩下那块石头的重量。
        '''
        bucket = [0] * 1001
        for i in stones:
            bucket[i] += 1
        slow = len(bucket) - 1
        while slow > 0:
            if bucket[slow] % 2 != 0:
                fast = slow - 1
                while fast > 0 and bucket[fast] == 0:
                    fast -= 1
                if fast == 0: break
                bucket[fast] -= 1
                bucket[slow - fast] += 1
            slow -= 1
        return slow
        '''

        '''
        # 1.排序
        while len(stones) > 1:
            stones.sort()
            s1 = stones.pop()
            s2 = stones.pop()
            stones.append(s1 - s2)
        return stones[0]
        '''
# @lc code=end

