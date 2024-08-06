class Solution:
   def minimumPushes(self, word: str) -> int:
       idx = 0
       freq_map = collections.Counter(word)
       freq_map = sorted(list(freq_map.items()), key=lambda x: -x[1])

       presses = 1
       res = 0
       for k, v in freq_map:
           res += presses * v
           idx += 1
           idx %= 8
           if idx == 0:
               presses += 1
       
       return res
