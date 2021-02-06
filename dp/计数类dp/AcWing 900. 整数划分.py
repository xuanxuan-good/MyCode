'''
2021.2.6 lzx
AcWing 900. 整数划分 题解：https://www.acwing.com/activity/content/code/content/804857/
一个正整数n可以表示成若干个正整数之和，形如：n=n1+n2+…+nk，其中n1≥n2≥…≥nk,k≥1。我们将这样的一种表示称为正整数n的一种划分。
现在给定一个正整数n，请你求出n共有多少种不同的划分方法。

输入格式
共一行，包含一个整数n。

输出格式
共一行，包含一个整数，表示总划分数量。
由于答案可能很大，输出结果请对109+7取模。

数据范围
1≤n≤1000

输入样例:
5
输出样例：
7
'''



# 完全背包问题
n = int(input())
mod = 1e9 + 7
f = [0] * (n + 1)

f[0] = 1
for i in range(1, n + 1):
    for j in range(i, n + 1):
        f[j] = (f[j] + f[j - i]) % mod

print(int(f[n]))



# 另一种思路，所有总和是i, 恰好表示成j个数和 的方案
n = int(input())
mod = 1e9 + 7
f = [[0] * (n + 1) for _ in range(n + 1)]

f[0][0] = 1
for i in range(1, n + 1):
    for j in range(1, i + 1):
        f[i][j] = (f[i - 1][j - 1] + f[i - j][j]) % mod

ans = 0
for i in range(1, n + 1):
    ans = (ans + f[n][i]) % mod
print(int(ans))