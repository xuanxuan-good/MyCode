'''
2020.02.01 lzx
AcWing 4. 多重背包问题题解：https://www.acwing.com/activity/content/code/content/779470/
（每件物品只能选s[i]次）
有 N 种物品和一个容量是 V 的背包。
第 i 种物品最多有 si 件，每件体积是 vi，价值是 wi。
求解将哪些物品装入背包，可使物品体积总和不超过背包容量，且价值总和最大。
输出最大价值。

输入格式
第一行两个整数，N，V，用空格隔开，分别表示物品种数和背包容积。
接下来有 N 行，每行三个整数 vi,wi,si，用空格隔开，分别表示第 i 种物品的体积、价值和数量。

输出格式
输出一个整数，表示最大价值。

数据范围
0<N,V≤100
0<vi,wi,si≤100

输入样例
4 5
1 2 3
2 4 1
3 4 3
4 5 2
输出样例：
10
'''


# 多重背包，数据量不大，O(nms) ---> 10^6, 可以通过
n, m = map(int, input().split())
v, w, s = [0] * (n + 1), [0] * (n + 1), [0] * (n + 1)
f = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    v[i], w[i], s[i] = map(int, input().split())

for i in range(1, n + 1):
    for j in range(m + 1):
        k = 0
        while j >= k * v[i] and k <= s[i]:
            f[i][j] = max(f[i][j], f[i - 1][j - v[i] * k] + w[i] * k)
            k += 1

print(f[n][m])