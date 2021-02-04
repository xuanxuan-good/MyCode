'''
2121.2.4 lzx
AcWing 895. 最长上升子序列 题解：https://www.acwing.com/activity/content/code/content/794431/
给定一个长度为N的数列，求数值严格单调递增的子序列的长度最长是多少。

输入格式
第一行包含整数N。第二行包含N个整数，表示完整序列。

输出格式
输出一个整数，表示最大长度。

数据范围
1≤N≤1000，
−109≤数列中的数≤109

输入样例：
7
3 1 2 1 8 5 6

输出样例：
4
'''


n = int(input())
nums = list(map(int, input().split()))
f = [1] * n

for i in range(1, n):
    for j in range(i):
        if nums[i] > nums[j]:
            f[i] = max(f[i], f[j] + 1)

print(max(f))