class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        def count_vowels(s):
            vowels = set("aeiouAEIOU")
            count = 0
            for char in s:
                if char in vowels:
                    count += 1
            return count

        n = len(s)
        mid = n // 2
        first_half = s[:mid]
        second_half = s[mid:]

        return count_vowels(first_half) == count_vowels(second_half)
