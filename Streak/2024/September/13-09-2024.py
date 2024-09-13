class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        pref = [*accumulate(arr, xor, initial = 0)]
        return [pref[l] ^ pref[r+1] for l, r in queries]   
