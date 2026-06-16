class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS = [0] * 26
        
        for i in range(len(s)):
            countS[ord(s[i])-ord('a')] += 1
            countS[ord(t[i])-ord('a')] -= 1
        
        for c in countS:
            if c != 0:
                return False
        return True