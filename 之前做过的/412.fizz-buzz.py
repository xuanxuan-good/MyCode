#
# @lc app=leetcode.cn id=412 lang=python3
#
# [412] Fizz Buzz
#

# @lc code=start
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        # hash O(n) O(1)
        ans = []
        fizz_buzz_dict = {3: "Fizz", 5: "Buzz"}
        for num in range(1, n+1):
            ans_num_str = ""
            for key in fizz_buzz_dict.keys():
                if num % key == 0:
                    ans_num_str += fizz_buzz_dict.get(key)
            if not ans_num_str:
                ans_num_str += str(num)
            ans.append(ans_num_str)
        return ans

        '''
        # 模拟法
        res = []
        for num in range(1, n+1):
            if num % 3 == 0 and num % 5 == 0:  #先判断，容易搞错
                res.append("FizzBuzz")
            elif num % 3 == 0:
                res.append("Fizz")
            elif num % 5 == 0:
                res.append("Buzz")
            else:
                res.append(str(num))
        return res
        '''

        '''
        # str连接 O(n) O(1)
        ans = []
        for num in range(1, n+1):
            ans_num_str = ""
            divideby3 = (num % 3 == 0)
            divideby5 = (num % 5 == 0)
            if divideby3:
                ans_num_str += "Fizz"
            if divideby5:
                ans_num_str += "Buzz"
            if not ans_num_str:
                ans_num_str += str(num)
            ans.append(ans_num_str)
        return ans
        '''

# @lc code=end

