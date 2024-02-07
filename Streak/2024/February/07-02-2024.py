class Solution:
    def frequencySort(self, s: str) -> str:
        return "".join([char * times for char, times in collections.Counter(s).most_common()])
        
