'''
2121.2.4 lzx
AcWing 898. 数字三角形 题解：https://www.acwing.com/activity/content/code/content/794217/
给定一个如下图所示的数字三角形，从顶部出发，在每一结点可以选择移动至其左下方的结点或移动至其右下方的结点，一直走到底层，
要求找出一条路径，使路径上的数字的和最大。

        7
      3   8
    8   1   0
  2   7   4   4
4   5   2   6   5

输入格式
第一行包含整数n，表示数字三角形的层数。
接下来n行，每行包含若干整数，其中第 i 行表示数字三角形第 i 层包含的整数。

输出格式
输出一个整数，表示最大的路径数字和。

数据范围
1≤n≤500,
−10000≤三角形中的整数≤10000

输入样例：
5
7
3 8
8 1 0 
2 7 4 4
4 5 2 6 5

输出样例：
30
'''



# 自底向上 √
n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
f = arr[-1]

for i in range(n - 2, -1, -1):
    for j in range(len(arr[i])):
        f[j] = max(f[j], f[j + 1]) + arr[i][j]

print(f[0])



# 自顶向下，要考虑边界问题
n = int(input())
arr = [[0]]
for _ in range(n):
    arr.append([0] + list(map(int, input().split())) + [0])
f = [[-1e9] * (n + 1) for _ in range(n + 1)]

f[1][1] = arr[1][1]
for i in range(2, n + 1):
    for j in range(1, i + 1):
        f[i][j] = max(f[i - 1][j - 1], f[i - 1][j]) + arr[i][j]

print(max(f[n]))
