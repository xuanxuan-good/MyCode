#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 堆 数组长度为n 空间复杂度O(n) 时间复杂度O(klogn) 堆的一次操作需要logn
        res = []
        occurences = collections.Counter(nums)
        max_heap = [(-val, key) for key, val in occurences.items()]
        heapq.heapify(max_heap)
        for i in range(k):
            res.append(heapq.heappop(max_heap)[1])
        return res

        '''
        # 桶分类
        freq, result = Counter(nums), []  # 每个数出现次数；结果列表
        inverse_freq = defaultdict(list)  # 用户自定义字典
        for k1,v1 in freq.items():
            inverse_freq[v1].append(k1)  # 反过来放置在自定义字典中
        for x in range(len(nums), 0, -1):  # 倒序遍历nums长度
            if x in inverse_freq:  # 如果x在出现的次数里
                result.extend(inverse_freq[x])  # x对应的值加入到结果中
                if len(result) >= k:
                    break  # 长度为k就 停止加入结果中
        return result[:k]
        '''

        '''
        # 快速排序+二变形？--partition索引的地方优点乱
        counter = collections.Counter(nums)  # 统计每个数出现的次数
        val = list(counter.keys())  # 有不重复的哪些数
        # print(counter.get(val[0]))  # 3 次数
        # print(val)
        l, r = 0, len(val) - 1  # 双指针
        while l <= r:
            pivot = self.partition(val, l, r, counter)
            if pivot == k - 1:
                return val[:k]  # 如果分区值是k-1索引对应的值，则返回前k个即可
            if pivot > k - 1:
                r = pivot - 1  # 前k个在左侧，缩到左侧即可
            else:
                l = pivot + 1  # 否则在右侧找分区

    def partition(self, val, l, r, counter):
        ran = random.randint(l, r)  # 找任意分区点
        val[ran], val[r] = val[r], val[ran]  # 任意值 和 右侧值交换
        pivot = r
        right = l  # 指针对应的索引位置
        for i in range(l, r):  # 遍历val中每一个值
            if counter.get(val[i]) >= counter.get(val[pivot]):  # 当前值 大于等于 分区值
                val[i], val[right] = val[right], val[i]  # 当前值和左侧值交换
                right += 1  # 左侧值加一
        val[right], val[pivot] = val[pivot], val[right]  # 遍历结束后，左侧值和分区值交换
        return right  # 返回的是分区值
        '''

        '''
        # 先找出每个数字出现的次数，然后将出现次数进行排序，找前k个 O(nlogn)
        a = collections.Counter(nums)
        # print(a.items())
        b = sorted(a.items(), key = lambda x:x[1], reverse = True)
        # print(b)
        return [b[i][0] for i in range(k)]
        '''
# @lc code=end

