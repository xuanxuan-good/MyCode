'''
2021.2.6 lzx
AcWing 291. 蒙德里安的梦想 题解：https://www.acwing.com/activity/content/code/content/806791/
求把N*M的棋盘分割成若干个1*2的的长方形，有多少种方案。
例如当N=2，M=4时，共有5种方案。当N=2，M=3时，共有3种方案。（横着或竖着）

输入格式
输入包含多组测试用例。每组测试用例占一行，包含两个整数N和M。
当输入用例N=0，M=0时，表示输入终止，且该用例无需处理。

输出格式
每个测试用例输出一个结果，每个结果占一行。

数据范围
1≤N,M≤11

输入样例：
1 2
1 3
1 4
2 2
2 3
2 4
2 11
4 11
0 0
输出样例：
1
0
1
2
3
5
144
51205
'''


# 数据量小于20的时候可以考虑状态压缩，太大变成二进制状态就会超时
N = 12
M = 1 << N
st = [True] * (M)
f = [[0] * (M) for _ in range(N)]

n, m = map(int, input().split())
while m or n:
    # 初始化
    for i in range(len(f)):
        for j in range(len(f[0])):
            f[i][j] = 0
    for i in range(len(st)):
        st[i] = True

    for i in range(1 << n):
        cnt = 0
        for j in range(n):
            if i >> j & 1:
                if cnt & 1: st[i] = False
                cnt = 0
            else: cnt += 1
        if cnt & 1: st[i] = False

    f[0][0] = 1

    # 状态转移
    for i in range(1, m + 1):
        for j in range(1 << n):
            for k in range(1 << n):
                if j & k == 0 and st[j | k]:
                    f[i][j] += f[i - 1][k]

    # 输出结果
    print(f[m][0])

    n, m = map(int, input().split())