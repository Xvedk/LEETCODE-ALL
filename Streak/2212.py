class Solution(object):
    def maxScore(self, s):
        ones_counter, zeros_counter = 0, 0
        score = -1
        currscore = 0

        for i in range(len(s)):
            if s[i] == '1':
                ones_counter += 1

        for i in range(len(s) - 1):
            if s[i] == '0':
                zeros_counter += 1
            else:
                ones_counter -= 1

            currscore = zeros_counter + ones_counter

            if currscore > score:
                score = currscore

        return score
