 #
# @lc app=leetcode.cn id=1122 lang=python3
#
# [1122] 数组的相对排序
#

# @lc code=start
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        cnt = collections.Counter(arr1)  # 非稀疏
        ans = []
        for x in arr2:
            if cnt[x]:
                ans.extend([x] * cnt.pop(x))
        for y in range(max(arr1)+1):
            if cnt[y]:
                ans.extend([y] * cnt.pop(y))
        return ans

        '''
        # 计数排序  [0,1000]范围不大，也可以考虑不基于比较的排序
        upper = max(arr1)  # 根据数组中的最大值 定义数组frequency
        frequency = [0] * (upper + 1)
        for x in arr1:
            frequency[x] += 1  # 记录每一个元素在arr1中出现的次数
        
        ans = list()
        for x in arr2:
            ans.extend([x] * frequency[x])  # 遍历arr2，x*出现次数 加到ans中
            frequency[x] = 0  # 加过去之后对应的值清零
        # 此时arr2中有的数已经放置好了
        for x in range(upper + 1):
            if frequency[x] > 0:
                ans.extend([x] * frequency[x])  # 剩下的数遍历后依次放置在最后即可
        return ans
        '''

        '''
        # 一个值进行比较
        def my_cmp(x):
            return rank[x] if x in rank else x
        n = len(arr2)
        rank = {x: i-n for i, x in enumerate(arr2)}
        arr1.sort(key=my_cmp)
        return arr1
        '''

        '''
        # 使用排序并自定义比较函数
        # 对于数组arr2中的第i个元素，将（arr[i],i）这一键值对放入哈希表rank中，方便对arr1中元素比较
        def mycmp(x):
            return (0, rank[x]) if x in rank else (1, x)
        # 如果是都拥有的数，则比较对应位置，靠前的还在前边，靠后的还在后边；
        # arr2中的数在arr1中没有，则比较剩下数的大小
        rank = {x: i for i, x in enumerate(arr2)}
        arr1.sort(key=mycmp)  # 如果arr1中的值在arr2中，（0，rankx）;不在（1，x）
        return arr1
        '''
# @lc code=end

