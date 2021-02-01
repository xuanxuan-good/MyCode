'''
2020.02.01 lzx
AcWing 9. 分组背包问题题解：https://www.acwing.com/activity/content/code/content/779435/
（每种物品只能选一个）
有 N 组物品和一个容量是 V 的背包。
每组物品有若干个，同一组内的物品最多只能选一个。
每件物品的体积是 vij，价值是 wij，其中 i 是组号，j 是组内编号。
求解将哪些物品装入背包，可使物品总体积不超过背包容量，且总价值最大。
输出最大价值。

输入格式
第一行有两个整数 N，V，用空格隔开，分别表示物品组数和背包容量。
接下来有 N 组数据：
每组数据第一行有一个整数 Si，表示第 i 个物品组的物品数量；
每组数据接下来有 Si 行，每行有两个整数 vij,wij，用空格隔开，分别表示第 i 个物品组的第 j 个物品的体积和价值；

输出格式
输出一个整数，表示最大价值。

数据范围
0<N,V≤100
0<Si≤100
0<vij,wij≤100

输入样例
3 5
2
1 2
2 4
1
3 4
1
4 5
输出样例：
8
'''


# 分组背包问题 1496ms O(nms) 10^6
n, m = map(int, input().split())
s = [0] * (n + 1)
N = 110
v, w = [[0] * N for _ in range(n + 1)], [[0] * N for _ in range(n + 1)]
f = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    s[i] = int(input())
    for j in range(s[i]):
        v[i][j], w[i][j] = map(int, input().split())

for i in range(1, n + 1):
    for j in range(m + 1):
        f[i][j] = f[i - 1][j]
        k = 0
        while k < s[i]:
            if j >= v[i][k]:
                f[i][j] = max(f[i][j], f[i - 1][j - v[i][k]] + w[i][k])
            k += 1

print(f[n][m])



# 完全背包问题优化，1388ms 滚动数组
n, m = map(int, input().split())
s = [0] * (n + 1)
N = 110
v, w = [[0] * N for _ in range(n + 1)], [[0] * N for _ in range(n + 1)]
f = [0] * (m + 1)

for i in range(1, n + 1):
    s[i] = int(input())
    for j in range(s[i]):
        v[i][j], w[i][j] = map(int, input().split())

for i in range(1, n + 1):
    for j in range(m, - 1, -1):
        k = 0
        while k < s[i]:
            if j >= v[i][k]:
                f[j] = max(f[j], f[j - v[i][k]] + w[i][k])
            k += 1

print(f[m])