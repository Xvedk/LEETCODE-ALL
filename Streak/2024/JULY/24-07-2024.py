class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        
        def mapInt(n):
            if not n:
                return mapping[0]
            res, pos = 0, 1
            while n:
                res += mapping[n % 10] * pos
                pos *= 10
                n //= 10
            return res
        # Creates a dictionary with n as the key and a tuple in the form (mapped_value, index)
        pairs = {n : (mapInt(n), idx) for idx, n in enumerate(nums)}

        return sorted(nums, key=lambda x: pairs[x]) # Our key for sorting is the tuple returned by the pairs dictionary
