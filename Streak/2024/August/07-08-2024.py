class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        def one(num):
            switcher = {
                1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five",
                6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"
            }
            return switcher.get(num, "")

        def two_less_20(num):
            switcher = {
                10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen",
                15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen"
            }
            return switcher.get(num, "")

        def ten(num):
            switcher = {
                2: "Twenty", 3: "Thirty", 4: "Forty", 5: "Fifty",
                6: "Sixty", 7: "Seventy", 8: "Eighty", 9: "Ninety"
            }
            return switcher.get(num, "")

        def two(num):
            if not num:
                return ""
            elif num < 10:
                return one(num)
            elif num < 20:
                return two_less_20(num)
            else:
                tenner = num // 10
                rest = num - tenner * 10
                return ten(tenner) + ('' if not rest else ' ' + one(rest))

        def three(num):
            hundred = num // 100
            rest = num - hundred * 100
            if hundred and rest:
                return one(hundred) + " Hundred " + two(rest)
            elif not hundred and rest:
                return two(rest)
            elif hundred and not rest:
                return one(hundred) + " Hundred"
            else:
                return ""

        billion = num // 1_000_000_000
        million = (num // 1_000_000) % 1_000
        thousand = (num // 1_000) % 1_000
        remainder = num % 1_000

        res = ""
        if billion:
            res += three(billion) + " Billion"
        if million:
            res += (" " if res else "") + three(million) + " Million"
        if thousand:
            res += (" " if res else "") + three(thousand) + " Thousand"
        if remainder:
            res += (" " if res else "") + three(remainder)

        return res.strip()
