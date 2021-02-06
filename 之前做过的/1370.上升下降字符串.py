#
# @lc app=leetcode.cn id=1370 lang=python3
#
# [1370] 上升下降字符串
#

# @lc code=start
class Solution:
    def sortString(self, s: str) -> str:
        '''
        # 记录每个数出现的次数，分别升序和降序遍历26个字母，存在的就放在res后边
        cnt, res, asc = collections.Counter(s), [], True
        while len(res) < len(s):
            for i in range(26):
                c = string.ascii_lowercase[i if asc else ~i]  # 获取整数对应的ASCII字母
                if cnt[c] > 0:
                    res.append(c)
                    cnt[c] -= 1
            asc = not asc
        return ''.join(res)
        '''
        cnt, ans, asc = collections.Counter(s), [], True
        while cnt:                                                                  # if Counter not empty.
            for c in sorted(cnt.keys()) if asc else reversed(sorted(cnt.keys())):   # traverse keys in ascending/descending order.
                ans.append(c)                                                       # append the key.
                cnt[c] -= 1                                                         # decrease the count.
                if cnt[c] == 0:                                                     # if the count reaches to 0.
                    del cnt[c]                                                      # remove the key from the Counter.
            asc = not asc                                                           # change the direction, same as asc ^= True.
        return ''.join(ans)
# @lc code=end

