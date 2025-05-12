from collections import Counter
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        possible_nums = range(100, 1000, 2)
        digit_dic = Counter(digits)
        def possible(number):
            num_str = str(number)
            num1, num2, num3 = int(num_str[0]), int(num_str[1]), int(num_str[2])
            if num1 != num2 != num3 != num1:
                return num1 in digit_dic and num2 in digit_dic and num3 in digit_dic
            if num1 == num2 == num3:
                return num1 in digit_dic and digit_dic[num1] >= 3
            if num1 == num2:
                return num1 in digit_dic and digit_dic[num1] >= 2 and num3 in digit_dic
            if num1 == num3:
                return num1 in digit_dic and digit_dic[num1] >= 2 and num2 in digit_dic
            if num2 == num3:
                return num2 in digit_dic and digit_dic[num2] >= 2 and num1 in digit_dic
        ans = []
        for number in possible_nums:
            if possible(number):
                ans.append(number)
        return ans
