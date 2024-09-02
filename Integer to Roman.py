class Solution:

    roman_digits = [
        # 1's, 5's, 10's
        ('I',  'V', 'X'),   # Ones
        ('X',  'L', 'C'),   # Tens
        ('C',  'D', 'M'),   # Hundreds
        ('M',  None, None)  # Thousands
    ]

    def intToRoman(self, num: int) -> str:
        if num > 3999 or num < 1:
            raise Exception()

        roman = ''

        for ones, fives, tens in self.roman_digits:
            if num == 0:
                return roman
            roman = self._generate_roman_numeral_for_one_through_nine(ones, fives, tens, num) + roman
            num = num // 10

        return roman

    def _generate_roman_numeral_for_one_through_nine(self, ones, fives, tens, num):
        five_mod = num % 5
        ten_mod  = num % 10

        tmp_roman = ''

        if tens is not None:
            if ten_mod == 9:
                return f'{ones}{tens}'
            elif ten_mod == 5:
                return fives

            if five_mod == 4:
                return f'{ones}{fives}'
            elif ten_mod > 5:
                tmp_roman = fives

        return tmp_roman + ones * five_mod
