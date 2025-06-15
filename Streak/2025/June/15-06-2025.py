class Solution:
    def maxDiff(self, num: int) -> int:
        str_num1 = str(num)
        str_num2 = str(num)

        # For first time (maximize by replacing one digit with '9')
        x = str_num1[0]
        y = '9'
        if x == '9':
            for i in str_num1:
                if i != '9':
                    x = i
                    break
        a = str_num1.replace(x, y)

        # For second time (minimize by replacing one digit with '0' or '1')
        x = ''
        if str_num2[0] != '1':
            x = str_num2[0]
            y = '1'
        else:
            for i in str_num2[1:]:
                if i != '0' and i != '1':
                    x = i
                    y = '0'
                    break
        b = str_num2 if x == '' else str_num2.replace(x, y)

        return abs(int(a) - int(b))
