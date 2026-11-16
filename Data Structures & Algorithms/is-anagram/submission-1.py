class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq = {}
        freqTwo = {}
        for i in range(len(s)):
            freq[s[i]] = freq.get(s[i], 0) + 1
            freqTwo[t[i]] = freqTwo.get(t[i], 0) + 1
        for char in freq:
            if freq.get(char, 0) != freqTwo.get(char, 0):
                return False
        return True