# 二分,长度相等，分别考虑两个数组的中位数a,b，如果相等则返回该中位数；如果a小，则去掉a数组前半部分 以及 b数组后半部分；b小则去掉b前半和a后半
# nums1, nums2 = [1,3,4], [2,5,7]  # 123456 -> 3.5
nums1, nums2 = [1,2,6,9], [0,5,7,8]  # 01256789
n = len(nums1)

# k = (n + n + 1)//2
left = 0
right = n
while left < right :
    m1 = left +(right - left)//2
    m2 = n - m1
    if nums1[m1] < nums2[m2-1]:
        left = m1 + 1  # 相当于去除nums1左半部分
    else:
        right = m1
m1 = left
m2 = k - m1 
c1 = max(nums1[m1-1] if m1 > 0 else float("-inf"), nums2[m2-1] if m2 > 0 else float("-inf") )
if (n + n) % 2 == 1:
    print( c1)
c2 = min(nums1[m1] if m1 < n else float("inf"), nums2[m2] if m2 <n else float("inf"))
print( (c1 + c2) / 2)