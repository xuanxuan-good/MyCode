'''
2021.2.4 lzx 
AcWing 896. 最长上升子序列 II 题解：https://www.acwing.com/activity/content/code/content/796625/
给定一个长度为N的数列，求数值严格单调递增的子序列的长度最长是多少。

输入格式
第一行包含整数N。第二行包含N个整数，表示完整序列。

输出格式
输出一个整数，表示最大长度。

数据范围
1≤N≤100000，
−109≤数列中的数≤109

输入样例：
7
3 1 2 1 8 5 6

输出样例：
4
'''


n = int(input())
nums = list(map(int, input().split()))
f = [0] * (n + 1)
len = 0

for i in range(n):
    l, r = 0, len
    while l < r:
        mid = l + r + 1 >> 1
        # 找小于nums[i]里的最大数，下一个位置就是nums[i]要放置的位置
        if f[mid] < nums[i]: l = mid
        else: r = mid - 1
    len = max(len, r + 1)
    f[r + 1] = nums[i]

print(len)