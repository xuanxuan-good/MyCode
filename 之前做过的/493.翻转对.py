#
# @lc app=leetcode.cn id=493 lang=python3
#
# [493] 翻转对
#

# @lc code=start
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        # 1.暴力，两次loop，找对应的值即可  2.merge_sort O(nlogn) O(n) √ 2.树状数组
        return self.merge_sort(nums, 0, len(nums)-1)
    def merge_sort(self, nums, left, right):
        if left >= right:
            return 0
        mid = (right + left) >> 1
        count = self.merge_sort(nums, left, mid) + self.merge_sort(nums, mid+1, right)
        j = t = mid+1
        cache = []
        for i in range(left, mid+1):
            while j <= right and nums[i] > 2*nums[j]:
                j += 1
            count += j - mid - 1
            while t <= right and nums[t] < nums[i]:
                cache.append(nums[t])
                t += 1
            cache.append(nums[i])
        while t <= right:  # 
            cache.append(nums[t])
            t += 1
        nums[left: right+1] = cache
        return count
        '''
        return self.merge_sort(nums, 0, len(nums)-1)
    def merge_sort(self, nums, left, right):
        if left >= right:
            return 0
        mid = (left + right) >> 1
        count = self.merge_sort(nums, left, mid) + self.merge_sort(nums, mid+1, right)  # 此处已经merge好了
        cache = []
        i = t = left
        for j in range(mid+1, right+1):
            while i <= mid and nums[i] <= 2 * nums[j]:  # 为什么要小于等于，nums已经是排好序的了
                i += 1
            count += mid - i + 1  # 因为要求的是>
            while t <= mid and nums[t] < nums[j]:
                cache.append(nums[t])
                t += 1
            cache.append(nums[j])
        while t <= mid:
            cache.append(nums[t])  # 比j大的 赋值
            t += 1
        nums[left:right+1] = cache
        return count
        '''

        '''
        return self.merge_sort(nums, 0, len(nums)-1)
    def merge_sort(self, nums, left, right):
        if left >= right:
            return 0
        mid = (left + right) >> 1
        cnt = self.merge_sort(nums, left, mid) + self.merge_sort(nums, mid + 1, right)
        j = mid + 1
        for i in range(left, mid+1):
            while j <= right and nums[i]/2 > nums[j]:
                j += 1
            cnt += j-(mid+1)
        self.merge(nums, left, mid, right)
        # nums[left:right+1] = sorted(nums[left:right+1])  # 直接用sort总的时间复杂度会变为O(nlogn logn)
        return cnt
    def merge(self, nums, left, mid, right):
        temp = []
        i = left
        j = mid + 1
        while i <= mid and j <= right:
            if nums[i] <= nums[j]:
                temp.append(nums[i])
                i += 1
            else:
                temp.append(nums[j])
                j += 1
        while i <= mid:
            temp.append(nums[i])
            i += 1
        while j <= right:
            temp.append(nums[j])
            j += 1
        nums[left: right + 1] = temp
        '''
# @lc code=end

