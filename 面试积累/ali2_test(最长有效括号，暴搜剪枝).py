'''
1.描述：给定一串由(、)、[、]、{、}组成的括号序列，输出最长的合法括号序列长度。合法括号序列定义如下：
1. 空括号序列是合法的
2. 若括号序列A合法，则(A)、[A]、{A}也是合法的
3. 若括号序列A和B均合法，则AB也是合法的
输入：括号序列
输出：最长合法序列长度
样例1 
输入: ({({(({()}})}{())})})[){{{([)()((()]]}])[{)]}{[}{)
输出: 4
'''

'''
# 思路：因为有最长字眼，所以考虑用dp来做
    用dp[i]表示 从开始到第i个下标结尾的字符 组成的最长合法括号序列长度
    需要根据i位置处字符是什么进行判断。
    1. s[i] = '(' i处字符不能和前边的i-1处字符进行匹配。dp[i] = 0
    2. s[i] = ')' 此时有可能与前边的字符匹配，需要根据s[i - 1]是什么进行判断
       [1] s[i - 1] = '(' 此时下标i与i-1处的字符是能匹配上的; i-1 处是'(',dp[i - 1] = 0; dp[i - 2]是之前的最长长度，dp[i] = dp[i - 2] + 2
       [2] s[i - 1] = ')' 下标i与i-1处的字符不匹配，((A))情况下有匹配的可能；否则dp[i] = 0.
            要找到与s[i]对应的位置：i - dp[i - 1] - 1, s[i - dp[i - 1] - 1]是‘(’，则是一对合法的括号：d[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2]
                                                                                                                这里相当于是AB形式，还需要把A处有效括号的长度加上
这里多了两种括号，[],{}, 判断条件都是相同的，加上相应判断即可
'''

# # 只有（）代码
# def VaildSequence(s):
#     n = len(s)
#     if n == 0:
#         return 0
#     res = 0
#     dp = [0] * n
#     for i in range(1, n):
#         if s[i] == ')':
#             if s[i - 1] == '(':
#                 dp[i] = 2
#                 if i - 2 >= 0:
#                     dp[i] += dp[i - 2]
#             elif i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
#                 dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2
#     return max(dp)

# s = '({({(({()}})}{())})})[){{{([)()((()]]}])[{)]}{[}{)'  # 4
# # s = ''  # 0
# # s = '()'  # 2
# res = VaildSequence(s)
# print(res)

'''
# 三种括号都有代码
def VaildSequence(s):
    n = len(s)
    if n == 0:
        return 0
    res = 0
    dp = [0] * n
    for i in range(1, n):
        if (s[i] == ')' and s[i - 1] == '(') or (s[i] == ']' and s[i - 1] == '[') or (s[i] == '}' and s[i - 1] == '{'):
            dp[i] = 2
            if i - 2 >= 0:
                dp[i] += dp[i - 2]
        elif (s[i] == ')' and i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(') or (s[i] == ']' and i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '[') or (s[i] == '}' and i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '{'):
                dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2
    return max(dp)

# s = '({({(({()}})}{())})})[){{{([)()((()]]}])[{)]}{[}{)'  # 4
# s = ''  # 0
# s = '()'  # 2
s = '()()([(]))'  # 4
res = VaildSequence(s)
print(res)
'''
# 栈的解法？



'''
2.描述：快递公司需要配送N个包裹，第i个包裹的重量为Ci，包裹无法分割。
每辆车最多可以配送的重量之和不超过W，最少多少辆车可以把包裹装完？
输入：N、W、包裹重量数组C。
输出：一个整数，表示最少需要多少辆车。
数据范围：1≤N≤18，1≤Ci≤W≤108
样例1
输入: 4 5 [2,1,2,4]
输出: 2
样例2
输入: 5 6 [5,2,4,1,6]
输出: 3
'''

import sys

# 第u个包裹，第K辆车
def dfs(u, k):
    global ans
    # 剪枝, 比ans大的肯定不符合条件
    if k >= ans: return
    # 反之k < ans,找到了最后一个包裹, 重新赋值并返回
    if u == n:
        ans = k
        return

    # 枚举放在哪辆车上
    for i in range(k):
        # 可行性剪枝：如果当前包裹加上去不超过 允许的最大重量，可以向这个方向搜
        if sums[i] + c[u] <= w:
            sums[i] += c[u]
            dfs(u + 1, k)  # 下一个包裹，还是这辆车
            sums[i] -= c[u]  # 恢复现场

    # 新开一辆车
    sums[k] = c[u]
    dfs(u + 1, k + 1)
    sums[k] = 0

if __name__ == '__main__':
    ins = sys.stdin.readline()
    in1, in2, in3 = ins.split()
    n, w = int(in1), int(in2)
    c = [int(i) for i in in3 if ord('0') <= ord(i) <= ord('9')]
    # print(n, w, c)

    # 1.优化搜索顺序，从大到小进行搜索，也就是从分支数最小的开始搜索
    c.sort(reverse = True)
    # print(c)
    # 记录每辆车放了多少重量的包裹, 结果是ans
    sums = [0] * n
    ans = n
    dfs(0, 0)

    print(ans)
