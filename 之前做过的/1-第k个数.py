# 有些数的素因子只有 3，5，7，请设计一个算法找出第 k 个数。
# 注意，不是必须有这些素因子，而是必须不包含其他的素因子。
# 例如，前几个数按顺序应该是 1，3，5，7，9，15，21。
class Solution:
    def getKthMagicNumber(self, k: int) -> int:
        # 丑数？ 动态规划，也可以理解为三个指针
        kth = [1, 3, 5, 7]
        if k <= 4:
            return kth[k-1]
        i3, i5, i7 = 1, 1, 1
        for i in range(4, k):
            k3, k5, k7 = 3 * kth[i3], 5 * kth[i5], 7 * kth[i7]
            kmin = min(k3, k5, k7)
            if kmin == k3:
                i3 += 1
            if kmin == k5:
                i5 += 1
            if kmin == k7:
                i7 += 1
            kth.append(kmin)
            # print(kth)
        return kth[-1]
s = Solution()
print(s.getKthMagicNumber(4))
'''
        # 98%
        nums = [3, 5, 7]
        heap = [(1, 1)]
        
        for _ in range(k):
            res, flag = heapq.heappop(heap)
            for num in nums:
                if flag <= num:  # 利用flag直接去重
                    heapq.heappush(heap, (res * num, num))
        return res
        '''

        '''
        nums = [3, 5, 7]
        heap = [1]
        
        for _ in range(k):
            res = heapq.heappop(heap)
            while heap and res == heap[0]:  # 在堆顶去重
                res = heapq.heappop(heap)
            for num in nums:
                heapq.heappush(heap, res * num)
        return res
        '''

        '''
        nums = [3, 5, 7]
        heap = [1]
        dedu = set([1])
        
        for _ in range(k):
            res = heapq.heappop(heap)
            for num in nums:
                cur = res * num
                if cur not in dedu:  # 用集合set去重
                    dedu.add(cur)
                    heapq.heappush(heap, cur)
        return res
        '''